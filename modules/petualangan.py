import time

class Petualangan:
    def __init__(self, json_manager, animations):
        self.json_manager = json_manager
        self.anim = animations
    
    def start_adventure(self):
        try:
            self.anim.type_text("\n🗺️ PETUALANGAN AREK JATIM 🌋", 0.03)
            self.anim.type_text("Ayo jelajahi kekayaan budaya dan sejarah Jawa Timur! 🏯", 0.03)
            print()
            
            input("Tekan Enter untuk memulai petualangan... ")
            
            petualangan_data = self.json_manager.load_data("petualangan.json")
            if not petualangan_data or "scenes" not in petualangan_data:
                print("❌ Data petualangan tidak ditemukan!")
                input("Tekan Enter untuk kembali...")
                return
            
            current_scene = "start"
            adventure_path = []
            
            while current_scene in petualangan_data["scenes"]:
                scene = petualangan_data["scenes"][current_scene]
                
                print("\n" + "═" * 60)
                self.anim.type_text(scene["text"], 0.02)
                print("═" * 60)
                
                # Jika scene memiliki ending, akhiri petualangan
                if "ending" in scene:
                    adventure_path.append(scene["ending"])
                    self.show_ending(scene, adventure_path)
                    break
                
                # Tampilkan pilihan jika ada
                if "choices" not in scene or not scene["choices"]:
                    print("❌ Tidak ada pilihan yang tersedia!")
                    break
                    
                print("\n🎯 Pilihan sampeyan:")
                for i, choice in enumerate(scene["choices"], 1):
                    print(f"   {i}. {choice['text']}")
                
                # Input pilihan
                while True:
                    try:
                        pilihan = input(f"\n🎯 Pilih opo rek? (1-{len(scene['choices'])}) ➤ ").strip()
                        if not pilihan:
                            continue
                            
                        pilihan_idx = int(pilihan) - 1
                        if 0 <= pilihan_idx < len(scene["choices"]):
                            next_scene = scene["choices"][pilihan_idx]["next"]
                            
                            # Cek apakah scene berikutnya ada
                            if next_scene not in petualangan_data["scenes"]:
                                print(f"❌ Scene '{next_scene}' tidak ditemukan! Kembali ke awal.")
                                current_scene = "start"
                            else:
                                current_scene = next_scene
                                adventure_path.append(scene["choices"][pilihan_idx]["text"])
                            break
                        else:
                            print("❌ Pilihan tidak valid! Coba lagi.")
                    except ValueError:
                        print("❌ Masukkan angka saja!")
                    except KeyboardInterrupt:
                        print("\n\n⚠️ Petualangan dihentikan...")
                        return
            
            # Simpan progress petualangan
            user_data = self.json_manager.load_current_user()
            if user_data:
                user_data["progress_petualangan"] = {
                    "status": "selesai",
                    "ending": adventure_path[-1] if adventure_path else "Belum selesai",
                    "path": adventure_path,
                    "jenis_ending": scene.get("type", "unknown") if 'scene' in locals() else "unknown"
                }
                self.json_manager.save_user_data(user_data)
                print("\n💾 Progress petualangan berhasil disimpan!")
                
        except Exception as e:
            print(f"❌ Error di petualangan: {e}")
            import traceback
            traceback.print_exc()
        
        input("\nTekan Enter untuk kembali ke menu...")
    
    def show_ending(self, scene, adventure_path):
        """Tampilkan ending petualangan"""
        print("\n" + "🎊" * 20)
        self.anim.pulse_effect("🎉 PETUALANGAN SELESAI! 🎉")
        print("🎊" * 20)
        
        ending_type = scene.get("type", "good")
        ending_emoji = self.get_ending_emoji(ending_type)
        
        # Tampilkan jenis ending sesuai permintaan
        ending_labels = {
            "good": "GOOD ENDING",
            "bad": "BAD ENDING", 
            "funny": "FUNNY ENDING",
            "secret": "SECRET ENDING",
            "neutral": "NEUTRAL ENDING"
        }
        
        ending_label = ending_labels.get(ending_type, "ENDING")
        
        print(f"\n{ending_emoji} {ending_label}: {scene['ending']}")
        print(f"📖 {scene['text']}")
        
        print(f"\n🗺️ Perjalanan sampeyan:")
        for i, step in enumerate(adventure_path, 1):
            print(f"   {i}. {step}")
        
        # Berikan komentar berdasarkan ending type
        comment = self.get_ending_comment(ending_type)
        print(f"\n💬 {comment}")
        
        # Tampilkan achievement khusus
        achievement = self.get_ending_achievement(ending_type)
        print(f"🏆 {achievement}")
    
    def get_ending_emoji(self, ending_type):
        """Dapatkan emoji berdasarkan jenis ending"""
        emojis = {
            "good": "🎉",
            "bad": "💔", 
            "funny": "😂",
            "secret": "🔮",
            "neutral": "⚖️"
        }
        return emojis.get(ending_type, "🎯")
    
    def get_ending_comment(self, ending_type):
        """Dapatkan komentar berdasarkan jenis ending"""
        comments = {
            "good": "Mantap pol rek! Sampeyan wes dadi petualang sejati! 🔥",
            "bad": "Yowes, nek seng dienggo sinau. Sakjane urip iku pilihan! 💪", 
            "funny": "Wes pokoke seneng-seneng wae rek! Yang penting happy! 😄",
            "secret": "WOIIII!!! Sampeyan nemu ending rahasia! Sakti tenan! ✨",
            "neutral": "Lumayan rek! Pengalaman sing tak lali-lalikan! 👍"
        }
        return comments.get(ending_type, "Petualangan yang menarik!")
    
    def get_ending_achievement(self, ending_type):
        """Dapatkan achievement berdasarkan jenis ending"""
        achievements = {
            "good": "Pencapaian: Petualang Sukses!",
            "bad": "Pelajaran: Hidup adalah pilihan!",
            "funny": "Kocakan: Bikin ketawa se-Jatim!",
            "secret": "Rahasia: Penemu Jalur Tersembunyi!",
            "neutral": "Pengalaman: Cerita yang berkesan!"
        }
        return achievements.get(ending_type, "Petualangan selesai!")
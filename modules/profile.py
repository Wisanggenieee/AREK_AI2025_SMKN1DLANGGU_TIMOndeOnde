import time

class Profile:
    def __init__(self, json_manager, animations):
        self.json_manager = json_manager
        self.anim = animations
    
    def show_profile(self):
        """Tampilkan profil user dengan data yang tersimpan"""
        try:
            # ✅ LOAD DATA USER TERBARU
            user_data = self.json_manager.load_current_user()
            
            if not user_data:
                print("\n❌ Durung ono data user rek!")
                print("💡 Mbok menawa sampeyan durung nggawe profil?")
                input("\nTekan Enter untuk balik...")
                return
            
            print("\n" + "═" * 60)
            self.anim.pulse_effect("👤 PROFIL SAMPEYAN")
            print("═" * 60)
            
            # DATA DASAR
            print(f"📛 Nama: {user_data.get('nama', 'Unknown')}")
            print(f"🏙️  Asal: {user_data.get('asal', 'Jawa Timur')}")
            print(f"📅 Tanggal Daftar: {user_data.get('tanggal_daftar', 'Unknown')}")
            
            # SKOR KUIS
            skor_kuis = user_data.get('skor_kuis', 0)
            print(f"📊 Skor Kuis Terakhir: {skor_kuis:.1f}%")
            
            # BADGE BERDASARKAN SKOR
            badge, pesan = self.get_badge(skor_kuis)
            print(f"🏆 Badge: {badge}")
            print(f"💬 {pesan}")
            
            # KOLEKSI GACHA
            koleksi = user_data.get('koleksi_gacha', [])
            print(f"🎁 Total Koleksi Gacha: {len(koleksi)} item")
            
            if koleksi:
                print("\n🎒 Item Koleksimu:")
                rare_items = [item for item in koleksi if item.get('rarity') in ['epic', 'ultra rare', 'legendary']]
                if rare_items:
                    for item in rare_items[-5:]:  # Tampilkan 5 rare terakhir
                        rarity_color = self.get_rarity_color(item.get('rarity', 'common'))
                        print(f"   - {item['nama']} ({rarity_color})")
                else:
                    print("   - Durung ono item langka")
            
            # HISTORY KUIS
            history = user_data.get('history_kuis', [])
            if history:
                print(f"\n📈 Total Main Kuis: {len(history)} kali")
                if history:
                    skor_tertinggi = max([h.get('skor', 0) for h in history])
                    print(f"🎯 Skor Tertinggi: {skor_tertinggi:.1f}%")
            
            # PROGRESS PETUALANGAN
            progress = user_data.get('progress_petualangan', {})
            status = progress.get('status', 'belum_mulai')
            ending = progress.get('ending')
            
            if status == 'selesai' and ending:
                print(f"\n🗺️  Petualangan Terakhir: {ending}")
            elif status == 'sedang_berlangsung':
                print(f"\n🗺️  Petualangan: Sedang berlangsung...")
            else:
                print(f"\n🗺️  Petualangan: Durung mulai")
            
            print("═" * 60)
            
        except Exception as e:
            print(f"\n❌ Error nampilkno profil: {e}")
        
        input("\nTekan Enter untuk balik ke menu...")
    
    def get_badge(self, persentase):
        """Berikan badge berdasarkan skor kuis"""
        if persentase >= 90:
            return "⭐⭐⭐⭐⭐ Legenda Jawa Timur", "Sak jati-jatine wong Jatim rek! 🔥🐯"
        elif persentase >= 80:
            return "⭐⭐⭐⭐ Macan Timur", "Wes sakti kowe!"
        elif persentase >= 70:
            return "⭐⭐⭐ Arek Asli Jatim", "Wani pol!"
        elif persentase >= 60:
            return "⭐⭐ Jagoan Kampung", "Lumayan ng Jatim!"
        elif persentase > 0:
            return "⭐ Jatim Pemula", "Sing penting niat e rek!"
        else:
            return "🎯 Belum Main Kuis", "Ayo main kuis dulu rek!"
    
    def get_rarity_color(self, rarity):
        """Warna untuk rarity item"""
        colors = {
            "common": "Biasa",
            "rare": "Biru", 
            "epic": "Ungu",
            "ultra rare": "Emas",
            "legendary": "Legendary 🔥"
        }
        return colors.get(rarity, "Biasa")
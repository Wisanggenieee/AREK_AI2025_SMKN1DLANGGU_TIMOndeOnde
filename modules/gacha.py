import random
import time

class Gacha:
    def __init__(self, json_manager, animations):
        self.json_manager = json_manager
        self.anim = animations
    
    def get_rarity_comment(self, rarity):
        """Komentar berdasarkan rarity item"""
        comments = {
            "common": "Lumayan rek, sing penting usaha! 👍",
            "rare": "Hoki mulai dateng nih! 😊", 
            "epic": "Wes makin sakti kowe! 🔥",
            "ultra rare": "Sakjane hoki kowe iki! 😎",
            "legendary": "WOIIII LEGENDARY!!! JACKPOT!!! 🎊🎊🎊"
        }
        return comments.get(rarity, "Mantap pol!")
    
    def open_gacha(self):
        try:
            self.anim.type_text("\n🎁 GACHA JATIM 🎁✨", 0.03)
            self.anim.type_text("Ayo bukak gacha dan kumpulin item-item khas Jatim! 😍", 0.03)
            print()
            
            input("   Tekan Enter buat bukak gacha... ")
            
            self.anim.loading_dots("\n   🔮 Membuka gacha misterius", 3)
            
            print("\n   ✨ " + "="*30 + " ✨")
            
            for i in range(3):
                print(f"   {'🎲' * (i+1)}", end='\r')
                time.sleep(0.3)
            
            gacha_data = self.json_manager.load_data("gacha.json")
            if not gacha_data or "items" not in gacha_data:
                print("   ❌ Data gacha tidak ditemukan!")
                input("   Tekan Enter untuk kembali...")
                return
                
            items = gacha_data["items"]
            weights = {
                "common": 40,
                "rare": 30, 
                "epic": 20,
                "ultra rare": 8,
                "legendary": 2
            }
            
            rarity_weights = [weights[item["rarity"]] for item in items]
            item_didapat = random.choices(items, weights=rarity_weights)[0]
            
            print("\n   " + "🎊" * 10)
            self.anim.pulse_effect("   GACHA WES METU REK!!")
            print("   " + "🎊" * 10)
            
            print(f"\n   ✨ Itemmu: {item_didapat['nama']}")
            print(f"   ⭐ Rarity: {item_didapat['rarity'].upper()}")
            
            komentar = self.get_rarity_comment(item_didapat["rarity"])
            print(f"   💬 {komentar}")
            
            # ✅ SIMPAN KE USER DATA DENGAN BENAR
            user_data = self.json_manager.load_current_user()
            
            if user_data is None:
                print("   ❌ Data user tidak ditemukan!")
                input("   Tekan Enter untuk kembali...")
                return
            
            if "koleksi_gacha" not in user_data:
                user_data["koleksi_gacha"] = []
            
            item_sudah_ada = any(item.get('id') == item_didapat.get('id') for item in user_data["koleksi_gacha"])
            
            if not item_sudah_ada:
                user_data["koleksi_gacha"].append(item_didapat)
                self.json_manager.save_user_data(user_data)
                self.anim.type_text("\n   ✅ Item berhasil ditambahke nang koleksimu!", 0.03)
            else:
                print("\n   ℹ️ Item iki wes ono nang koleksimu!")
            
            total_koleksi = len(user_data.get("koleksi_gacha", []))
            print(f"\n   📦 Total koleksimu: {total_koleksi} item")
            
            if user_data["koleksi_gacha"]:
                print("\n   🎒 Koleksimu:")
                for item in user_data["koleksi_gacha"][-5:]:
                    item_name = item.get('nama', 'Unknown Item')
                    item_rarity = item.get('rarity', 'common')
                    print(f"      - {item_name} ({item_rarity})")
            
            print("\n   " + "═" * 40)
            
        except Exception as e:
            print(f"   ❌ Error di gacha: {e}")
        
        input("\n   Tekan Enter untuk kembali ke menu... ")
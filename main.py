import time
import os
import sys

# Tambahkan path ke sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

try:
    from utils.json_manager import JSONManager
    from modules.animations import Animations
    from modules.quiz import Quiz
    from modules.gacha import Gacha
    from modules.petualangan import Petualangan
    from modules.profile import Profile
    from modules.info import Info
except ImportError as e:
    print(f"❌ Error: {e}")
    print("💡 Pastikan struktur folder sudah benar!")
    input("Tekan Enter untuk keluar...")
    sys.exit(1)

class JatimGame:
    def __init__(self):
        self.json_manager = JSONManager()
        self.anim = Animations()
        self.quiz = Quiz(self.json_manager, self.anim)
        self.gacha = Gacha(self.json_manager, self.anim)
        self.petualangan = Petualangan(self.json_manager, self.anim)
        self.profile = Profile(self.json_manager, self.anim)
        self.info = Info(self.anim)
        self.current_user = None
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_logo(self):
        logo = """
    ╔═══════════════════════════════════════════════╗
    ║       🐯 SEBERAPA JATIM SIH KAMU? 🐯         ║
    ║     🔥 Budaya | Tradisi | Identitas 🔥       ║
    ╚═══════════════════════════════════════════════╝
        """
        print(logo)
        self.anim.type_text("\n    🎉 Sugeng rawuh nang CLI paling rame sak Jatim! 🎊\n", 0.03)
    
    def start_screen(self):
        self.clear_screen()
        self.anim.progress_bar("Memuat kekayaan budaya Jawa Timur...", 3)
        self.clear_screen()
        self.show_logo()
        time.sleep(2)
    
    def welcome_screen(self):
        self.clear_screen()
        
        self.anim.type_text("✨ HALO REK! ✨", 0.05)
        print()
        self.anim.type_text("Sugeng rawuh nang petualangan budaya Jawa Timur...", 0.03)
        print()
        self.anim.type_text("Ayo bukti'no seberapa Jatim sih kamu? 😉", 0.03)
        print("\n" + "═" * 60)
        
        self.anim.type_text("\n📛 Sopo jenengmu rek?", 0.03)
        nama = input(" ➤ ").strip()
        if not nama:
            nama = "Player"
        
        self.anim.type_text("\n🏙️  Kowe teko kota/kabupaten opo nang Jatim?", 0.03)
        asal = input(" ➤ ").strip()
        if not asal:
            asal = "Jawa Timur"
        
        self.anim.loading_dots("\n💾 Nyimpen data sampeyan", 3)
        
        komentar, emoji = self.get_kota_comment(asal)
        print(f"\n🎯 {emoji} {komentar}")
        
        self.current_user = {
            "nama": nama,
            "asal": asal,
            "skor_kuis": 0,
            "koleksi_gacha": [],
            "progress_petualangan": {"status": "belum_mulai", "ending": None},
            "history_kuis": [],
            "tanggal_daftar": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_play_time": 0
        }
        
        self.json_manager.save_user_data(self.current_user)
        print("✅ Data sampeyan wes disimpen!")
        
        self.anim.countdown("Mulai dalam", 3)
    
    def get_kota_comment(self, kota):
        kota = kota.lower().strip()
        
        kota_data = {
            # Kota Metropolitan
            "surabaya": ("Wes Cak & Ning Suroboyo! Kota Pahlawan!", "🐂"),
            "malang": ("Wani perih? Arema pisan! Kota Apel!", "🍎"),
            "sidoarjo": ("Wong Sidoarjo siap gas poll! Kota Udang!", "🦐"),
            
            # Kota Madya
            "kediri": ("Kota tahu tak? Gudang rokok kretek!", "🚬"),
            "batu": ("Kota Wisata! Wes tau nang Jatim Park?", "🎡"),
            "blitar": ("Kota Patria! Lahar ilang nek durung mampir!", "🌋"),
            "pasuruan": ("Kota Gula! Manis koyo tebu!", "🎋"),
            "probolinggo": ("Kota Angin! Awas keblinger!", "💨"),
            "mojokerto": ("Kota Onde-onde! Pusaka Majapahit!", "🏺"),
            
            # Kabupaten Jawa Timur Barat
            "jombang": ("Kota Santri! Gus Dur punyo kene!", "📿"),
            "lamongan": ("Kota Soto! Soto Lamongan juara!", "🍜"),
            "gresik": ("Kota Semen! Industri teko kene!", "🏭"),
            "tuban": ("Kota Tuak! Bumi wali sing sakti!", "🥃"),
            "bojonegoro": ("Kota Ledok! Sumber minyak Jatim!", "🛢️"),
            "nganjuk": ("Kota Angkrek! Simbol persatuan!", "⚔️"),
            "madiun": ("Kota Pecel! Arek Madiun sing trengginas!", "🥬"),
            "magetan": ("Kota Gethuk! Lereng Gunung Lawu!", "🍠"),
            "ngawi": ("Kota Ledre! Pintu gerbang Jatim!", "🚪"),
            
            # Kabupaten Jawa Timur Selatan
            "pacitan": ("Kota Seribu Goa! Pantai selatan Jatim!", "🏖️"),
            "ponorogo": ("Kota Reog! Warok sing sakti mandraguna!", "🎭"),
            "trenggalek": ("Kota Lontong! Kopi lan durian!", "☕"),
            "tulungagung": ("Kota Marmer! Kerajinan marmer nomer siji!", "🗿"),
            "lumajang": ("Kota Pisang! Salak lan apel!", "🍌"),
            "jember": ("Kota Tembakau! Karnaval sing rame!", "🎪"),
            
            # Kabupaten Jawa Timur Timur
            "banyuwangi": ("Using Pride! Gandrung lan kopi ijen!", "💃"),
            "bondowoso": ("Kota Tape! Kopi arabika juara!", "🍶"),
            "situbondo": ("Kota Salak! Mangga lan jeruk!", "🐍"),
            
            # Pulau Madura
            "bangkalan": ("Soko Bangkalan! Karapan sapi nomer siji!", "🐎"),
            "sampang": ("Arek Sampang! Jembatan Suramadu wes dibangun!", "🌉"),
            "pamekasan": ("Kota Batik! Batik Madura cerah lan cantik!", "🎨"),
            "sumenep": ("Kota Keris! Keris Madura terkenal sakti!", "⚔️")
        }
        
        for key, value in kota_data.items():
            if key in kota:
                return value
        
        return ("Lhoo rek, kok dudu Jatim? Gpp, tak Jatim'no kene 😎", "🌍")
    
    def main_menu(self):
        while True:
            self.clear_screen()
            
            # ✅ LOAD DATA USER TERBARU SETIAP KALI KE MENU
            latest_user = self.json_manager.load_current_user()
            if latest_user:
                self.current_user = latest_user
            
            menu = """
    ╔════════════════════ MENU UTAMA ═══════════════════╗
    ║ 🎯  1. Kuis Seberapa Jatim                    ║
    ║ 🗺️  2. Petualangan Arek Jatim                 ║
    ║ 🎁  3. Gacha Jatim                           ║
    ║ 👤  4. Profil Sampeyan                       ║
    ║ ℹ️  5. Informasi                              ║
    ║ 🚪  6. Keluar / Exit                          ║
    ╚═══════════════════════════════════════════════════╝
            """
            print(menu)
            
            # ✅ TAMPILKAN NAMA USER DI MENU
            if self.current_user:
                print(f"    👋 Halo, {self.current_user['nama']} dari {self.current_user['asal']}!")
                print("    " + "═" * 50)
            
            pilihan = input("    🎯 Pilih opo rek? ➤ ").strip()
            
            if pilihan == "1":
                self.quiz.start_quiz()
            elif pilihan == "2":
                self.petualangan.start_adventure()
            elif pilihan == "3":
                self.gacha.open_gacha()
            elif pilihan == "4":
                self.profile.show_profile()
            elif pilihan == "5":
                self.info.show_info()
            elif pilihan == "6":
                if self.confirm_exit():
                    break
            else:
                print("    ❌ Ora ono pilihan kuwi rek! 😅")
                time.sleep(1)
    
    def confirm_exit(self):
        """Konfirmasi sebelum keluar dari game dengan 2 opsi sederhana"""
        self.clear_screen()
        
        print("\n" + "⚠️" * 20)
        self.anim.pulse_effect("⛔ KONFIRMASI KELUAR")
        print("⚠️" * 20)
        
        # Pesan peringatan singkat
        warning_text = """
    ❗ PERHATIAN REK!
    
    🔸 Data progres TIDAK akan disimpan otomatis
    🔸 Screenshot dulu profil sampeyan biar aman
    🔸 Semua progres akan hilang untuk sesi berikutnya
    """
        
        self.anim.type_text(warning_text, 0.02)
        
        print("\n" + "═" * 50)
        print("    🎯 APA SAMPEYAN YAKIN PENGEN KELUAR?")
        print("═" * 50)
        
        # Hanya 2 opsi seperti yang diminta
        print("\n    🎯 PILIHAN:")
        print("    ✅ [Y] - Ya, yakin keluar")
        print("    ❌ [T] - Tidak, kembali ke menu")
        
        while True:
            konfirmasi = input("\n    🎯 Pilihan sampeyan (Y/T)? ➤ ").strip().upper()
            
            if konfirmasi == 'Y':
                self.exit_game()
                return True
            elif konfirmasi == 'T':
                print("\n    👍 Oke rek, balik nang menu main...")
                time.sleep(1)
                return False
            else:
                print("    ❌ Pilih Y atau T wae rek!")
    
    def exit_game(self):
        """Animasi keluar game"""
        self.clear_screen()
        
        print("\n" + "🎊" * 20)
        self.anim.pulse_effect("👋 SAMPEAN WES HEBAT REK!")
        print("🎊" * 20)
        
        # Tampilkan ringkasan progress terakhir
        user_data = self.json_manager.load_current_user()
        if user_data:
            print(f"\n    📈 Progress Akhir Sampeyan:")
            print(f"       🎯 Skor Kuis Terakhir: {user_data.get('skor_kuis', 0):.1f}%")
            print(f"       🎁 Total Koleksi: {len(user_data.get('koleksi_gacha', []))} item")
            print(f"       🗺️  Petualangan: {user_data.get('progress_petualangan', {}).get('ending', 'Belum selesai')}")
            
            # Berikan badge berdasarkan skor
            badge, pesan = self.get_exit_badge(user_data.get('skor_kuis', 0))
            print(f"       🏆 {badge}")
        
        farewell_text = """
    🤝 Matur suwun rek wis main bareng!
    💪 Semoga tambah Jatim dan bangga jadi arek Jatim!
    
    💾 JANGAN LUPA: 
       - Screenshot profil sampeyan
       - Simpan data progres manual  
       - Bagikan pencapaian ke teman-teman!
    
    👋 Sampai ketemu maneh nang petualangan sakwise! 😄
        """
        
        self.anim.type_text(farewell_text, 0.03)
        print("\n" + "═" * 60)
        
        self.anim.countdown("Keluar dalam", 3)
        self.clear_screen()
    
    def get_exit_badge(self, skor):
        """Berikan badge berdasarkan skor saat exit"""
        if skor >= 90:
            return "⭐⭐⭐⭐⭐ LEGENDA JATIM", "Sakjane arek Jatim sejati!"
        elif skor >= 80:
            return "⭐⭐⭐⭐ MACAN TIMUR", "Wes sakti pol!"
        elif skor >= 70:
            return "⭐⭐⭐ AREK ASLI", "Wani lan peduli!"
        elif skor >= 60:
            return "⭐⭐ JAGOAN KAMPUNG", "Lumayan ng Jatim!"
        elif skor > 0:
            return "⭐ JATIM PEMULA", "Sing penting usaha!"
        else:
            return "🎯 PECINTA JATIM", "Mbok menawa main kuis dulu?"
    
    def run(self):
        try:
            self.start_screen()
            self.welcome_screen()
            self.main_menu()
        except KeyboardInterrupt:
            print("\n\n❌ Program dihentikan mendadak...")
            print("💡 Data terakhir mungkin belum tersimpan!")
            print("📱 Sebaiknya screenshot progres sebelum keluar!")
            input("\nTekan Enter untuk keluar...")
        except Exception as e:
            print(f"\n\n💥 Error: {e}")
            input("Tekan Enter untuk keluar...")

if __name__ == "__main__":
    game = JatimGame()
    game.run()
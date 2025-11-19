import random
import time

class Quiz:
    def __init__(self, json_manager, animations):
        self.json_manager = json_manager
        self.anim = animations
    
    def start_quiz(self):
        self.anim.type_text("\n🎯 KUIS SEBERAPA JATIM KAMU? 📚🔥", 0.03)
        self.anim.type_text("Ayo bukti'no pengetahuanmu tentang Jawa Timur! 😎", 0.03)
        print()
        
        quiz_data = self.json_manager.load_data("quiz.json")
        if not quiz_data or "pertanyaan" not in quiz_data:
            print("❌ Data kuis tidak ditemukan!")
            input("Tekan Enter untuk kembali...")
            return
            
        pertanyaan = random.sample(quiz_data["pertanyaan"], min(5, len(quiz_data["pertanyaan"])))
        skor = 0
        
        for i, soal in enumerate(pertanyaan, 1):
            print(f"\n❓ Pertanyaan {i}/{len(pertanyaan)}")
            self.anim.type_text(f"{soal['pertanyaan']}", 0.02)
            print()
            
            for j, pilihan in enumerate(soal['pilihan']):
                print(f"   {chr(65+j)}) {pilihan}")
            
            jawaban = input("\n   🎯 Jawabanmu ➤ ").upper().strip()
            
            self.anim.loading_dots("   ⏳ Ngecek jawaban", 2)
            
            if jawaban and ord(jawaban) - 65 == soal['jawaban_benar']:
                self.anim.type_text("   🎉 Mantap pol rek! 🔥🔥🔥", 0.03)
                skor += 1
            else:
                jawaban_benar = chr(65 + soal['jawaban_benar'])
                self.anim.type_text(f"   😅 Yowes ra popo, ben ndang pinter.", 0.03)
                print(f"   💡 Jawaban bener: {jawaban_benar}")
            
            time.sleep(1)
        
        # Hitung persentase
        persentase = (skor / len(pertanyaan)) * 100
        
        # Berikan badge
        badge, pesan = self.get_badge(persentase)
        
        print("\n" + "═" * 50)
        self.anim.pulse_effect("🎊 HASIL AKHIR KUIS")
        print(f"   📊 Skor: {skor}/{len(pertanyaan)} ({persentase:.1f}%)")
        print(f"   🏆 Badge: {badge}")
        print(f"   💬 {pesan}")
        print("═" * 50)
        
        # ✅ SIMPAN HASIL DENGAN BENAR
        user_data = self.json_manager.load_current_user()
        if user_data:
            user_data["skor_kuis"] = persentase
            if "history_kuis" not in user_data:
                user_data["history_kuis"] = []
            user_data["history_kuis"].append({
                "skor": persentase,
                "total_soal": len(pertanyaan),
                "tanggal": time.strftime("%Y-%m-%d %H:%M:%S")
            })
            self.json_manager.save_user_data(user_data)
            print("   💾 Skor berhasil disimpan!")
        
        input("\n   Tekan Enter untuk balik ke menu...")
    
    def get_badge(self, persentase):
        if persentase >= 90:
            return "⭐⭐⭐⭐⭐ Legenda Jawa Timur", "Sak jati-jatine wong Jatim rek! 🔥🐯"
        elif persentase >= 80:
            return "⭐⭐⭐⭐ Macan Timur", "Wes sakti kowe!"
        elif persentase >= 70:
            return "⭐⭐⭐ Arek Asli Jatim", "Wani pol!"
        elif persentase >= 60:
            return "⭐⭐ Jagoan Kampung", "Lumayan ng Jatim!"
        else:
            return "⭐ Jatim Pemula", "Sing penting niat e rek!"
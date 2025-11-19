class Info:
      def __init__(self, animations):
         self.anim = animations
      
      def show_info(self):
         """Tampilkan informasi tentang program"""
         print("\n" + "═" * 60)
         self.anim.pulse_effect("ℹ️ INFORMASI PROGRAM")
         print("═" * 60)
         
         info_text = """
🎯 TENTANG PROGRAM:
   "SEBERAPA JATIM SIH KAMU?" 
   Game CLI interaktif untuk mengenal budaya Jawa Timur
   yang kaya akan sejarah, tradisi, dan kuliner.

🚀 FITUR UTAMA:
   • Kuis pengetahuan Jawa Timur
   • Petualangan interaktif 
   • Gacha item budaya Jatim
   • Profil dan progres pemain
   • Animasi CLI yang menarik

🛠️ TEKNOLOGI:
   • Dibuat dengan Python 3.x
   • Tanpa library eksternal
   • Penyimpanan data JSON
   • Full CLI experience

👨‍💻 DEVELOPER:
   • Wisanggeni Cahya Manggalar
   • Kharis Fatur Rohman

🏫 SEKOLAH:
   SMKN 1 DLANGGU

🎊 CREDITS:
   • AI Assistant: ChatGPT
   • Tema: Budaya Jawa Timur
   • Versi: 1.0
   • Tahun: 2025

💡 TUJUAN:
   Melestarikan dan mempopulerkan budaya Jawa Timur
   melalui media game yang edukatif dan menyenangkan!
        """
        
         self.anim.type_text(info_text, 0.01)
         print("═" * 60)
         input("\nTekan Enter untuk kembali ke menu...")
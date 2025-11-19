import time
import sys

class Animations:
    @staticmethod
    def type_text(text, speed=0.03):
        """Animasi ketik seperti mesin tik"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(speed)
        print()
    
    @staticmethod
    def progress_bar(text, duration=3):
        """Progress bar dengan animasi"""
        print(f"\n⏳ {text}")
        steps = ["■□□□□□□□□□ 10%", "■■■□□□□□□□ 30%", "■■■■■□□□□□ 50%", 
                "■■■■■■■□□□ 70%", "■■■■■■■■■□ 90%", "■■■■■■■■■■ 100%"]
        
        for step in steps:
            print(f"\r{step}", end="", flush=True)
            time.sleep(duration / len(steps))
        print("\n✅ Loading selesai! 🎉")
    
    @staticmethod
    def loading_dots(text, dots=3, speed=0.5):
        """Animasi loading dengan titik-titik"""
        print(text, end="", flush=True)
        for i in range(dots):
            print(".", end="", flush=True)
            time.sleep(speed)
        print()
    
    @staticmethod
    def countdown(text, seconds=3):
        """Animasi countdown"""
        print(f"\n⏰ {text}")
        for i in range(seconds, 0, -1):
            print(f"\r{i}...", end="", flush=True)
            time.sleep(1)
        print("\rMulai! 🚀")
    
    @staticmethod
    def pulse_effect(text, pulses=3):
        """Efek berdenyut pada teks"""
        for i in range(pulses):
            print(f"\r{text}{'!' * (i + 1)}", end="", flush=True)
            time.sleep(0.3)
        print()
    
    @staticmethod
    def celebrate(text):
        """Animasi celebrasi"""
        print(f"\n🎉 {text} 🎉")
        for emoji in ["🎊", "🎈", "🥳", "✨"]:
            print(f"\r{emoji}", end="", flush=True)
            time.sleep(0.2)
        print()
import json
import os

class JSONManager:
    def __init__(self):
        self.data_dir = "data"
        self.create_data_files()
    
    def create_data_files(self):
        """Buat folder dan file data jika belum ada"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        
        files_to_create = {
            "userdata.json": {},
            "quiz.json": self.create_quiz_data(),
            "gacha.json": self.create_gacha_data(),
            "petualangan.json": self.create_petualangan_data(),
            "info.json": self.create_info_data()
        }
        
        for filename, data in files_to_create.items():
            filepath = f"{self.data_dir}/{filename}"
            if not os.path.exists(filepath):
                self.save_data(filename, data)
    
    def load_current_user(self):
        """Load user data terbaru (yang terakhir disimpan)"""
        data = self.load_data("userdata.json")
        if data:
            # Ambil user terakhir yang disimpan
            return list(data.values())[-1] if data else None
        return None

    def create_quiz_data(self):
        """50 Pertanyaan tentang Jawa Timur"""
        return {
            "pertanyaan": [
                # SEJARAH & TOKOH (10 pertanyaan)
                {
                    "id": 1, "pertanyaan": "Kota mana di Jatim yang dijuluki 'Kota Pahlawan'?",
                    "pilihan": ["Surabaya", "Malang", "Mojokerto", "Kediri"], "jawaban_benar": 0
                },
                {
                    "id": 2, "pertanyaan": "Siapa pahlawan dari Jatim yang terkenal dengan sebutan 'Bung Tomo'?",
                    "pilihan": ["Sutomo", "Soekarno", "Hatta", "Sudirman"], "jawaban_benar": 0
                },
                {
                    "id": 3, "pertanyaan": "Kerajaan Hindu-Buddha terbesar di Jawa Timur adalah?",
                    "pilihan": ["Majapahit", "Singasari", "Kediri", "Kahuripan"], "jawaban_benar": 0
                },
                {
                    "id": 4, "pertanyaan": "Candi peninggalan Majapahit yang terkenal di Trowulan?",
                    "pilihan": ["Candi Bajang Ratu", "Candi Borobudur", "Candi Prambanan", "Candi Sewu"], "jawaban_benar": 0
                },
                {
                    "id": 5, "pertanyaan": "Raja terbesar Kerajaan Majapahit adalah?",
                    "pilihan": ["Hayam Wuruk", "Raden Wijaya", "Jayanegara", "Tribhuwana"], "jawaban_benar": 0
                },
                {
                    "id": 6, "pertanyaan": "Peristiwa 10 November 1945 terjadi di kota?",
                    "pilihan": ["Surabaya", "Malang", "Sidoarjo", "Gresik"], "jawaban_benar": 0
                },
                {
                    "id": 7, "pertanyaan": "Pahlawan nasional dari Blitar yang proklamator kemerdekaan?",
                    "pilihan": ["Soekarno", "Hatta", "Sudirman", "Kartini"], "jawaban_benar": 0
                },
                {
                    "id": 8, "pertanyaan": "Kerajaan sebelum Majapahit yang berpusat di Singosari?",
                    "pilihan": ["Singasari", "Kediri", "Kahuripan", "Jenggala"], "jawaban_benar": 0
                },
                {
                    "id": 9, "pertanyaan": "Bandara Internasional Juanda terletak di?",
                    "pilihan": ["Sidoarjo", "Surabaya", "Malang", "Gresik"], "jawaban_benar": 0
                },
                {
                    "id": 10, "pertanyaan": "Jembatan terpanjang di Indonesia yang menghubungkan Surabaya-Madura?",
                    "pilihan": ["Suramadu", "Ampera", "Barito", "Mahakam"], "jawaban_benar": 0
                },

                # GEOGRAFI & WISATA (15 pertanyaan)
                {
                    "id": 11, "pertanyaan": "Gunung tertinggi di Jawa Timur?",
                    "pilihan": ["Semeru", "Bromo", "Arjuno", "Kelud"], "jawaban_benar": 0
                },
                {
                    "id": 12, "pertanyaan": "Gunung berapi aktif yang terkenal dengan lautan pasirnya?",
                    "pilihan": ["Bromo", "Semeru", "Kelud", "Arjuno"], "jawaban_benar": 0
                },
                {
                    "id": 13, "pertanyaan": "Kawah dengan blue fire yang terkenal di dunia?",
                    "pilihan": ["Kawah Ijen", "Kawah Bromo", "Kawah Kelud", "Kawah Arjuno"], "jawaban_benar": 0
                },
                {
                    "id": 14, "pertanyaan": "Kota di Jatim yang dijuluki 'Kota Apel'?",
                    "pilihan": ["Malang", "Surabaya", "Pasuruan", "Batu"], "jawaban_benar": 3
                },
                {
                    "id": 15, "pertanyaan": "Kota di Jatim yang dijuluki 'Kota Angin'?",
                    "pilihan": ["Probolinggo", "Situbondo", "Banyuwangi", "Lumajang"], "jawaban_benar": 0
                },
                {
                    "id": 16, "pertanyaan": "Kota di Jatim yang dijuluki 'Kota Pisang'?",
                    "pilihan": ["Lumajang", "Jember", "Banyuwangi", "Bondowoso"], "jawaban_benar": 0
                },
                {
                    "id": 17, "pertanyaan": "Kota di Jatim yang dijuluki 'Kota Tape'?",
                    "pilihan": ["Bondowoso", "Lumajang", "Jember", "Banyuwangi"], "jawaban_benar": 0
                },
                {
                    "id": 18, "pertanyaan": "Wisata alam yang terkenal di Kota Batu?",
                    "pilihan": ["Jawa Timur Park", "Selecta", "Songgoriti", "Semua benar"], "jawaban_benar": 3
                },
                {
                    "id": 19, "pertanyaan": "Tempat wisata di Banyuwangi yang ada blue fire?",
                    "pilihan": ["Kawah Ijen", "Teluk Hijau", "Plengkung", "Pulau Merah"], "jawaban_benar": 0
                },
                {
                    "id": 20, "pertanyaan": "Kebun binatang tertua di Asia Tenggara?",
                    "pilihan": ["Kebun Binatang Surabaya", "Ragunan", "Gembira Loka", "Taman Safari"], "jawaban_benar": 0
                },
                {
                    "id": 21, "pertanyaan": "Museum transportasi terbesar di Asia?",
                    "pilihan": ["Museum Angkut", "Museum Kereta Api", "Museum Dirgantara", "Museum Bahari"], "jawaban_benar": 0
                },
                {
                    "id": 22, "pertanyaan": "Pantai yang terkenal di Malang Selatan?",
                    "pilihan": ["Balekambang", "Sendang Biru", "Ngliyep", "Semua benar"], "jawaban_benar": 3
                },
                {
                    "id": 23, "pertanyaan": "Gunung yang menjadi batas Jatim-Jateng?",
                    "pilihan": ["Lawu", "Wilis", "Kelud", "Arjuno"], "jawaban_benar": 0
                },
                {
                    "id": 24, "pertanyaan": "Pulau terbesar di Jatim setelah Pulau Jawa?",
                    "pilihan": ["Madura", "Bawean", "Kangean", "Raas"], "jawaban_benar": 0
                },
                {
                    "id": 25, "pertanyaan": "Taman nasional yang melindungi badak Jawa?",
                    "pilihan": ["Alas Purwo", "Baluran", "Meru Betiri", "Bromo Tengger"], "jawaban_benar": 2
                },

                # KULINER (15 pertanyaan)
                {
                    "id": 26, "pertanyaan": "Makanan khas Jatim yang terbuat dari daging sapi dan kuah hitam?",
                    "pilihan": ["Rawon", "Soto", "Rujak", "Pecel"], "jawaban_benar": 0
                },
                {
                    "id": 27, "pertanyaan": "Makanan khas Jatim 'Rujak Cingur' berasal dari kota?",
                    "pilihan": ["Surabaya", "Malang", "Madura", "Banyuwangi"], "jawaban_benar": 0
                },
                {
                    "id": 28, "pertanyaan": "Makanan khas Surabaya berupa lontong dengan tahu, tauge, dan lentho?",
                    "pilihan": ["Lontong Balap", "Lontong Kikil", "Lontong Opor", "Lontong Sayur"], "jawaban_benar": 0
                },
                {
                    "id": 29, "pertanyaan": "Soto ayam dengan koya khas Lamongan?",
                    "pilihan": ["Soto Lamongan", "Soto Madura", "Soto Ayam", "Soto Betawi"], "jawaban_benar": 0
                },
                {
                    "id": 30, "pertanyaan": "Makanan khas Jatim berupa nasi dengan lauk tahu tek?",
                    "pilihan": ["Nasi Pecel", "Nasi Rawon", "Nasi Campur", "Nasi Tumpang"], "jawaban_benar": 0
                },
                {
                    "id": 31, "pertanyaan": "Sate dengan bumbu kacang khas Madura?",
                    "pilihan": ["Sate Madura", "Sate Ponorogo", "Sate Kelinci", "Sate Ayam"], "jawaban_benar": 0
                },
                {
                    "id": 32, "pertanyaan": "Makanan khas Ponorogo?",
                    "pilihan": ["Sate Ponorogo", "Gulai Kambing", "Rawon", "Pecel"], "jawaban_benar": 0
                },
                {
                    "id": 33, "pertanyaan": "Makanan khas Madiun?",
                    "pilihan": ["Pecel Madiun", "Rawon", "Soto", "Rujak"], "jawaban_benar": 0
                },
                {
                    "id": 34, "pertanyaan": "Makanan khas Kediri?",
                    "pilihan": ["Tahu Takwa", "Tahu Gejrot", "Tahu Sumedang", "Tahu Bulat"], "jawaban_benar": 0
                },
                {
                    "id": 35, "pertanyaan": "Makanan khas Banyuwangi?",
                    "pilihan": ["Rujak Soto", "Pecel Rawon", "Soto Oseng", "Sego Tempong"], "jawaban_benar": 3
                },
                {
                    "id": 36, "pertanyaan": "Makanan khas Bondowoso?",
                    "pilihan": ["Tape Bondowoso", "Jenang Kudus", "Wingko Babat", "Klepon"], "jawaban_benar": 0
                },
                {
                    "id": 37, "pertanyaan": "Minuman khas Jatim dari buah kawista?",
                    "pilihan": ["Legin", "Wedang Ronde", "Bajigur", "Kopi Joss"], "jawaban_benar": 0
                },
                {
                    "id": 38, "pertanyaan": "Minuman khas Jatim dari jahe dan gula merah?",
                    "pilihan": ["Wedang Jahe", "Bajigur", "Bandrek", "Secang"], "jawaban_benar": 0
                },
                {
                    "id": 39, "pertanyaan": "Makanan khas Gresik?",
                    "pilihan": ["Pudak", "Lumpia", "Pastel", "Lemper"], "jawaban_benar": 0
                },
                {
                    "id": 40, "pertanyaan": "Makanan khas Trenggalek?",
                    "pilihan": ["Lontong", "Kupat", "Lemang", "Lemper"], "jawaban_benar": 0
                },

                # BUDAYA & KESENIAN (10 pertanyaan)
                {
                    "id": 41, "pertanyaan": "Kesenian Reog berasal dari daerah mana?",
                    "pilihan": ["Ponorogo", "Surabaya", "Madura", "Banyuwangi"], "jawaban_benar": 0
                },
                {
                    "id": 42, "pertanyaan": "Tari Gandrung berasal dari daerah mana?",
                    "pilihan": ["Banyuwangi", "Surabaya", "Madura", "Kediri"], "jawaban_benar": 0
                },
                {
                    "id": 43, "pertanyaan": "Kesenian Ludruk berasal dari daerah mana?",
                    "pilihan": ["Jombang", "Surabaya", "Lamongan", "Bojonegoro"], "jawaban_benar": 0
                },
                {
                    "id": 44, "pertanyaan": "Tari khas Jatim yang biasanya dibawakan penyambutan tamu?",
                    "pilihan": ["Tari Remo", "Tari Gandrung", "Tari Ngremo", "Tari Jejer"], "jawaban_benar": 0
                },
                {
                    "id": 45, "pertanyaan": "Kesenian Karapan Sapi berasal dari?",
                    "pilihan": ["Madura", "Surabaya", "Lamongan", "Bojonegoro"], "jawaban_benar": 0
                },
                {
                    "id": 46, "pertanyaan": "Upacara adat Suku Tengger di Gunung Bromo?",
                    "pilihan": ["Yadnya Kasada", "Nyepi", "Galungan", "Kuningan"], "jawaban_benar": 0
                },
                {
                    "id": 47, "pertanyaan": "Alat musik tradisional Jawa Timur?",
                    "pilihan": ["Gamelan", "Angklung", "Sasando", "Kolintang"], "jawaban_benar": 0
                },
                {
                    "id": 48, "pertanyaan": "Festival tahunan yang terkenal di Banyuwangi?",
                    "pilihan": ["Festival Gandrung Sewu", "Festival Reog", "Festival Ludruk", "Festival Kuda Lumping"], "jawaban_benar": 0
                },
                {
                    "id": 49, "pertanyaan": "Pakaian adat Jawa Timur?",
                    "pilihan": ["Pesa'an", "Kebaya", "Batik", "Sarung"], "jawaban_benar": 0
                },
                {
                    "id": 50, "pertanyaan": "Rumah adat Jawa Timur?",
                    "pilihan": ["Joglo", "Limasan", "Panggung", "Panjang"], "jawaban_benar": 0
                }
            ]
        }

    def create_gacha_data(self):
        """30 Item Gacha tentang Jawa Timur"""
        return {
            "items": [
                # LEGENDARY (3 items)
                {"id": 1, "nama": "🐯 Macan Jatim Legendary", "rarity": "legendary", "deskripsi": "Simbol keberanian wong Jatim"},
                {"id": 2, "nama": "👑 Mahkota Majapahit", "rarity": "legendary", "deskripsi": "Mahkota kerajaan terbesar Nusantara"},
                {"id": 3, "nama": "🌋 Blue Fire Ijen", "rarity": "legendary", "deskripsi": "Api biru langka dari Kawah Ijen"},
                
                # ULTRA RARE (5 items)
                {"id": 4, "nama": "🎭 Reog Ponorogo", "rarity": "ultra rare", "deskripsi": "Topeng dadak merak Ponorogo"},
                {"id": 5, "nama": "💃 Tari Gandrung", "rarity": "ultra rare", "deskripsi": "Tari penyambutan Banyuwangi"},
                {"id": 6, "nama": "🌉 Jembatan Suramadu", "rarity": "ultra rare", "deskripsi": "Jembatan terpanjang di Indonesia"},
                {"id": 7, "nama": "🏛️ Candi Bajang Ratu", "rarity": "ultra rare", "deskripsi": "Candi peninggalan Majapahit"},
                {"id": 8, "nama": "🎪 Karapan Sapi", "rarity": "ultra rare", "deskripsi": "Balapan sapi tradisional Madura"},
                
                # EPIC (8 items)
                {"id": 9, "nama": "🥘 Rawon Legendaris", "rarity": "epic", "deskripsi": "Kuah hitam khas dengan bumbu keluwek"},
                {"id": 10, "nama": "🐂 Surabaya Spirit", "rarity": "epic", "deskripsi": "Semangat arek Suroboyo"},
                {"id": 11, "nama": "🌋 Gunung Bromo", "rarity": "epic", "deskripsi": "Gunung berapi aktif yang mistis"},
                {"id": 12, "nama": "🎨 Batik Madura", "rarity": "epic", "deskripsi": "Batik dengan warna cerah khas Madura"},
                {"id": 13, "nama": "🌄 Air Terjun Tumpak Sewu", "rarity": "epic", "deskripsi": "Air terjun cantik di Lumajang"},
                {"id": 14, "nama": "🎵 Gamelan Jawa", "rarity": "epic", "deskripsi": "Alat musik tradisional Jawa"},
                {"id": 15, "nama": "🏭 Pabrik Semen Gresik", "rarity": "epic", "deskripsi": "Industri semen terbesar"},
                {"id": 16, "nama": "🎡 Jawa Timur Park", "rarity": "epic", "deskripsi": "Taman hiburan di Kota Batu"},
                
                # RARE (8 items)
                {"id": 17, "nama": "🌾 Kopi Bondowoso", "rarity": "rare", "deskripsi": "Kopi arabika dari lereng Gunung Ijen"},
                {"id": 18, "nama": "💃 Tari Remo", "rarity": "rare", "deskripsi": "Tari penyambutan tamu agung"},
                {"id": 19, "nama": "🍶 Anggur Brem", "rarity": "rare", "deskripsi": "Minuman fermentasi khas Madiun"},
                {"id": 20, "nama": "🏺 Gerabah Dinoyo", "rarity": "rare", "deskripsi": "Gerabah khas Malang"},
                {"id": 21, "nama": "🎭 Topeng Malang", "rarity": "rare", "deskripsi": "Topeng kayu khas Malang"},
                {"id": 22, "nama": "🍬 Gula Merah Madura", "rarity": "rare", "deskripsi": "Gula aren khas Pulau Madura"},
                {"id": 23, "nama": "☕ Kopi Lanang", "rarity": "rare", "deskripsi": "Kopi biji tunggal khas Jatim"},
                {"id": 24, "nama": "🍎 Apel Malang", "rarity": "rare", "deskripsi": "Buah apel segar dari Kota Malang"},
                
                # COMMON (6 items)
                {"id": 25, "nama": "🛵 Bebek Madura", "rarity": "common", "deskripsi": "Motor bebek kesayangan wong Madura"},
                {"id": 26, "nama": "🍜 Soto Lamongan", "rarity": "common", "deskripsi": "Soto ayam dengan koya khas Lamongan"},
                {"id": 27, "nama": "🍢 Sate Madura", "rarity": "common", "deskripsi": "Sate daging dengan bumbu kacang"},
                {"id": 28, "nama": "🍚 Nasi Pecel", "rarity": "common", "deskripsi": "Nasi dengan sayuran dan bumbu kacang"},
                {"id": 29, "nama": "☕ Wedang Jahe", "rarity": "common", "deskripsi": "Minuman hangat jahe khas Jatim"},
                {"id": 30, "nama": "🥬 Pecel Madiun", "rarity": "common", "deskripsi": "Salad sayur dengan bumbu kacang"}
            ]
        }

    def create_petualangan_data(self):
        """Data petualangan interaktif yang SUPER SERU dengan banyak ending!"""
        return {
            "scenes": {
                # === AWAL PETUALANGAN ===
                "start": {
                    "text": "🌅 PETUALANGAN AREK JATIM 🌅\n\nKowe lagi plesiran nang Trowulan, bekas ibukota Majapahit.\nTiba-tiba nemu peta kuno sing aneh! 🗺️\nPeta iki gambarno menuju harta karun Kerajaan Majapahit!\n\nApa sing arek kowe lakoni?",
                    "choices": [
                        {"text": "🚀 Langsung telusuri peta kuno!", "next": "telusuri_peta"},
                        {"text": "🗣️ Tanya warga sekitar dulu", "next": "tanya_warga"},
                        {"text": "🏛️ Lapor ke museum biar aman", "next": "lapor_museum"},
                        {"text": "🤫 Diam-diam simpan peta, riset dulu", "next": "riset_diam"}
                    ]
                },

                # === JALUR TELUSURI PETA ===
                "telusuri_peta": {
                    "text": "🛣️ JALUR CEPET: TELUSURI PETA!\n\nKowe nekad mlaku neng dalan sing ditunjuk peta.\nTiba-tiba nemu persimpangan:\n\n1. 🏞️ LEWAT TAMAN PURBAKALA - Konon ada teka-teki kuno\n2. 🌲 LEWAT HUTAN KERAMAT - Ada suara-suara misterius\n3. 🏔️ LEWAT GUNUNG KAWASAN - Jalur terjal tapi cepat",
                    "choices": [
                        {"text": "🏞️ Lewat Taman Purbakala", "next": "taman_purbakala"},
                        {"text": "🌲 Lewat Hutan Keramat", "next": "hutan_keramat"},
                        {"text": "🏔️ Lewat Gunung Kawasan", "next": "gunung_kawasan"},
                        {"text": "🔙 Balik ke awal", "next": "start"}
                    ]
                },

                "taman_purbakala": {
                    "text": "🏺 TAMAN PURBAKALA MISTERIUS\n\nKowe nemu taman purbakala sing sepi.\nOno prasasti kuno sing isine teka-teki:\n\n'Yang mencari harta tanpa ilmu\nBagai keris tanpa warangka'\n\nTiba-tiba ono suara dari balik patung...",
                    "choices": [
                        {"text": "🔍 Periksa prasasti lebih detail", "next": "prasasti_detail"},
                        {"text": "🏃‍♂️ Cepat minggat, serem!", "next": "minggat_serem"},
                        {"text": "🗣️ Panggil suara itu", "next": "panggil_suara"}
                    ]
                },

                "prasasti_detail": {
                    "text": "🔎 RAHASIA PRASASTI TERBUKA!\n\nKowe nemu simbol rahasia dibalik prasasti!\nSymbol iki nunjukno lokasi gua tersembunyi.\n\nTAPI... ono penjaga taman sing marahi kowe!",
                    "choices": [
                        {"text": "🤝 Jelaskan tujuan mulia", "next": "good_ending_arkeolog"},
                        {"text": "💨 Lari bawa simbol!", "next": "chase_sequence"},
                        {"text": "🎭 Pura-pura turis biasa", "next": "funny_ending_turis"}
                    ]
                },

                # === JALUR TANYA WARGA ===
                "tanya_warga": {
                    "text": "👥 JALUR WARGA: TANYA PENDUDUK\n\nKowe nemui sesepuh desa sing bijaksana.\nDheweke cerita:\n\n'Harta karun Majapahit iki dilindungi makhluk gaib.\nOno 3 ujian: Keberanian, Kebijaksanaan, dan Pengorbanan'\n\nDheweke nawani bantuan...",
                    "choices": [
                        {"text": "💪 Terima tantangan!", "next": "tiga_ujian"},
                        {"text": "😰 Takut, mending urungkan", "next": "urungkan_takut"},
                        {"text": "🕵️‍♂️ Minta petunjuk rahasia", "next": "petunjuk_rahasia"}
                    ]
                },

                "tiga_ujian": {
                    "text": "⚔️ TIGA UJIAN MAJAPAHIT\n\nSesepuh nuntun kowe nang 3 tempat ujian:\n\n1. 🦁 GUHA MACAN - Uji keberanian\n2. 🧠 TAMAN PUJANGGA - Uji kebijaksanaan  \n3. 💰 RUANG HARTA - Uji pengorbanan",
                    "choices": [
                        {"text": "🦁 Guha Macan dulu", "next": "guha_macan"},
                        {"text": "🧠 Taman Pujangga dulu", "next": "taman_pujangga"},
                        {"text": "💰 Ruang Harta dulu", "next": "ruang_harta"}
                    ]
                },

                "guha_macan": {
                    "text": "🦁 GUHA MACAN - UJI KEBERANIAN\n\nKowe nemu guha gelap.\nDari dalam ono auman macan sing nggeterke!\n\nTapi kowe liat, iki mung patung macan mekanik kuno!\nOno tombol rahasia dibalik patung...",
                    "choices": [
                        {"text": "🔼 Pencet tombol atas", "next": "secret_ending_macan"},
                        {"text": "🔽 Pencet tombol bawah", "next": "bad_ending_jebakan"},
                        {"text": "🚪 Kabur dari guha", "next": "escape_guha"}
                    ]
                },

                # === JALUR MUSEUM ===
                "lapor_museum": {
                    "text": "🏛️ JALUR RESMI: LAPOR MUSEUM\n\nKowe ketemu arkeolog muda sing antusias.\nDheweke seneng banget nemu peta kuno!\n\n'Tak bantu analisis peta iki!'\nTernyata peta iki nunjukno situs arkeologi baru!",
                    "choices": [
                        {"text": "🤝 Kerjasama ekspedisi", "next": "good_ending_penemu"},
                        {"text": "💼 Minta imbalan dulu", "next": "bad_ending_serakah"},
                        {"text": "📸 Dokumentasikan dulu", "next": "funny_ending_foto"}
                    ]
                },

                # === JALUR DIAM-DIAM ===
                "riset_diam": {
                    "text": "🕵️‍♂️ JALUR DETEKTIF: RISET DIAM-DIAM\n\nKowe pulang dulu, riset peta kuno iki.\nTernyata peta iki petunjuk menuju 'Perpustakaan Rahasia Majapahit'!\n\nTapi ono kelompok pemburu harta ilegal sing ngincar peta iki!",
                    "choices": [
                        {"text": "🔐 Cari perpustakaan rahasia", "next": "perpustakaan_rahasia"},
                        {"text": "🚔 Lapor polisi", "next": "lapor_polisi"},
                        {"text": "💸 Jual peta ke kolektor", "next": "bad_ending_pengkhianat"}
                    ]
                },

                "perpustakaan_rahasia": {
                    "text": "📚 PERPUSTAKAAN RAHASIA MAJAPAHIT!\n\nKowe nemu perpustakaan tersembunyi dibawah tanah!\nIsine ribuan naskah kuno sing durung pernah dibuka.\n\nOno 3 buku khusus:\n- Buku Sejarah Rahasia\n- Buku Ilmu Kuno  \n- Buku Ramalan Masa Depan",
                    "choices": [
                        {"text": "📖 Baca Sejarah Rahasia", "next": "secret_ending_sejarah"},
                        {"text": "🔮 Baca Ilmu Kuno", "next": "good_ending_ilmuwan"},
                        {"text": "🔮 Baca Ramalan Masa Depan", "next": "secret_ending_ramalan"}
                    ]
                },

                # === ENDING BAIK ===
                "good_ending_arkeolog": {
                    "text": "🎉 ENDING BAIK: AHLI ARKEOLOG!\n\nPenjaga ternyata arkeolog senior!\nDheweke kagum sama ketekunanmu.\n\nKowe diajak kerjasama ekskavasi situs bersejarah.\nJenengmu dicatat dalam sejarah arkeologi Indonesia!\n\n🏆 Pencapaian: Dikenal sebagai Penemu Situs Baru",
                    "ending": "Ahli Arkeolog Handal",
                    "type": "good"
                },

                "good_ending_penemu": {
                    "text": "🌟 ENDING BAIK: PENEMU SEJATI!\n\nBersama tim arkeolog, kowe nemu situs purbakala penting!\nTernyata 'harta karun' sejati adalah pengetahuan sejarah.\n\nKowe dapat penghargaan dari pemerintah dan diundang\nke berbagai seminar internasional!\n\n🏆 Pencapaian: Dihargai sebagai Penemu Sejati",
                    "ending": "Penemu Situs Bersejarah",
                    "type": "good"
                },

                "good_ending_ilmuwan": {
                    "text": "🔬 ENDING BAIK: ILMUWAN BRILIAN!\n\nDari buku ilmu kuno, kowe nemu ramuan tradisional\nyang bisa menyembuhkan penyakit modern!\n\nKowe jadi ilmuwan terkenal dan membantu banyak orang.\nHarta sejati adalah ilmu yang bermanfaat!\n\n🏆 Pencapaian: Penemu Ramuan Ajaib",
                    "ending": "Ilmuwan Brilian",
                    "type": "good"
                },

                # === ENDING JAHAT ===
                "bad_ending_serakah": {
                    "text": "💸 ENDING JAHAT: SERAKAH!\n\nKowe minta imbalan besar pada arkeolog.\nTernyata dheweke adalah kolektor barang ilegal!\n\nKowe ditipu dan peta kuno-mu dijual ke pasar gelap.\nKowe dapat uang, tapi kehilangan warisan budaya!\n\n💔 Peringatan: Jangan serakah!",
                    "ending": "Kolektor Serakah",
                    "type": "bad"
                },

                "bad_ending_jebakan": {
                    "text": "🚫 ENDING JAHAT: TERJEBAK!\n\nTombol bawah ternyata memicu jebakan kuno!\nKowe terkunci dalam guha selama 3 hari.\n\nAkhirnya diselamatkan tim penyelamat, tapi\npeta kuno-mu rusak dan harta karun hilang selamanya.\n\n💔 Peringatan: Hati-hati dengan pilihan!",
                    "ending": "Petualang Terjebak",
                    "type": "bad"
                },

                "bad_ending_pengkhianat": {
                    "text": "👿 ENDING JAHAT: PENGKHIANAT!\n\nKowe jual peta ke kolektor gelap.\nTernyata mereka menghancurkan situs bersejarah!\n\nKowe dapat uang banyak, tapi dikutuk masyarakat\nsebagai pengkhianat budaya Jawa Timur!\n\n💔 Peringatan: Hargai warisan leluhur!",
                    "ending": "Pengkhianat Budaya",
                    "type": "bad"
                },

                # === ENDING LUCU ===
                "funny_ending_turis": {
                    "text": "😂 ENDING LUCU: TURIS AWAM!\n\nKowe pura-pura jadi turis biasa.\nPenjaga kasih brosur wisata dan ngajak foto.\n\nTernyata kowe jadi model foto promosi wisata Trowulan!\nWajahmu ada di semua brosur turis selama setahun!\n\n📸 Pencapaian: Model Brosur Turis Terkenal",
                    "ending": "Model Brosur Turis",
                    "type": "funny"
                },

                "funny_ending_foto": {
                    "text": "🤳 ENDING LUCU: FOTO VIRAL!\n\nKowe sibuk dokumentasi buat Instagram.\nTiba-tiba ketiduran di museum karena kecapean.\n\nFoto tidurmu jadi meme viral #NgetripSampaiTidur!\nKowe dapat followers banyak, tapi lupa sama harta karun!\n\n😂 Pencapaian: Selebgram Museum Viral",
                    "ending": "Selebgram Museum",
                    "type": "funny"
                },

                # === ENDING RAHASIA ===
                "secret_ending_macan": {
                    "text": "🐯 ENDING RAHASIA: JAGA MACAN!\n\nTombol atas membuka ruang rahasia!\nTernyata 'harta karun' adalah MACAN JATIM LEGENDARY\nyang masih hidup dan terjaga selama 500 tahun!\n\nKowe ditunjuk sebagai penjaga baru macan suci!\nHidupmu berubah total jadi guardian budaya!\n\n🔮 Rahasia: Penjaga Macan Suci",
                    "ending": "Penjaga Macan Suci",
                    "type": "secret"
                },

                "secret_ending_sejarah": {
                    "text": "📜 ENDING RAHASIA: PENJAGA SEJARAH!\n\nBuku sejarah rahasia berisi catatan lengkap Majapahit.\nKowe menemukan bahwa leluhurmu adalah penasihat raja!\n\nKowe mewarisi tugas menjaga sejarah sejati Jawa Timur.\nHidupmu dipenuhi makna sebagai penjaga warisan!\n\n🔮 Rahasia: Penjaga Sejarah Sejati",
                    "ending": "Penjaga Sejarah",
                    "type": "secret"
                },

                "secret_ending_ramalan": {
                    "text": "🔮 ENDING RAHASIA: PERAMAL MASA DEPAN!\n\nBuku ramalan menunjukkan masa depan Jawa Timur!\nKowe bisa melihat perkembangan budaya 100 tahun mendatang.\n\nKowe jadi penasihat budaya pemerintah dan membantu\nmelestarikan tradisi untuk generasi mendatang!\n\n🔮 Rahasia: Visioner Budaya",
                    "ending": "Visioner Budaya",
                    "type": "secret"
                },

                # === SCENE TRANSISI ===
                "minggat_serem": {
                    "text": "🏃‍♂️ KOWE MINGGAT NANGIS-NANGIS!\n\nTernyata suara itu cuma kucing liar! 😹\nKowe balik ngomah malu-malu...",
                    "ending": "Petualang Penakut",
                    "type": "funny"
                },

                "escape_guha": {
                    "text": "🚶‍♂️ KOWE KELUAR DENGAN SELAMAT\n\nTapi kowe melewatkan kesempatan besar!\nMungkin lain kali lebih berani...",
                    "ending": "Petualang Hati-Hati",
                    "type": "neutral"
                },

                "urungkan_takut": {
                    "text": "😴 KOWE URUNGKAN NIAT\n\nKowe balik ngomah, tidur nyenyak.\nMimpi indah tentang harta karun...",
                    "ending": "Pemimpi Harta Karun",
                    "type": "neutral"
                },

                "lapor_polisi": {
                    "text": "👮 KOWE LAPOR POLISI\n\nPolisi menangkap kelompok pemburu harta ilegal.\nKowe dapat penghargaan dari kepolisian!",
                    "ending": "Warga Peduli Hukum",
                    "type": "good"
                },

                "chase_sequence": {
                    "text": "🏃‍♂️🏃‍♂️🏃‍♂️ ADU CEPAT!\n\nKowe dikejar penjaga taman!\nTapi kowe lebih cepat dan berhasil kabur!\n\nSayangnya simbol rahasia jatuh dan hilang...",
                    "ending": "Pelari Cepat Tapi Ceroboh",
                    "type": "funny"
                },

                "panggil_suara": {
                    "text": "🗣️ KOWE PANGGIL SUARA ITU\n\nTernyata suara itu dari peneliti muda yang\nsedang riset tentang simbol-simbol kuno!\n\nDiajak kerjasama, kowe nemu banyak temuan baru!",
                    "ending": "Partner Peneliti Muda",
                    "type": "good"
                },

                "petunjuk_rahasia": {
                    "text": "🤫 KOWE DAPAT PETUNJUK RAHASIA!\n\nSesepuh kasih petunjuk jalan pintas menuju\nruang harta tanpa melalui ujian!\n\nTapi... apakah ini jalan yang benar?",
                    "choices": [
                        {"text": "🛣️ Ikuti jalan pintas", "next": "bad_ending_shortcut"},
                        {"text": "⚔️ Tetap ikuti ujian", "next": "tiga_ujian"}
                    ]
                },

                "bad_ending_shortcut": {
                    "text": "⏩ ENDING JAHAT: JALAN PINTAS!\n\nJalan pintas ternyata jebakan!\nKowe terjebak dalam labirin tanpa akhir.\n\nHarta karun hanya ilusi, yang ada hanya penyesalan!",
                    "ending": "Pencari Jalan Pintas",
                    "type": "bad"
                },

                # === SCENE BARU UNTUK JALUR LAIN ===
                "hutan_keramat": {
                    "text": "🌲 HUTAN KERAMAT MISTERIUS\n\nKowe mlaku nang hutan sing angker.\nOno suara gemerisik dan bayangan aneh!\n\nTiba-tiba nemu pondok tua di tengah hutan...",
                    "choices": [
                        {"text": "🚪 Masuk ke pondok", "next": "pondok_tua"},
                        {"text": "🌳 Sembunyi di balik pohon", "next": "sembunyi_pohon"},
                        {"text": "🏃‍♂️ Lari sekencang-kencangnya", "next": "lari_ketakutan"}
                    ]
                },

                "pondok_tua": {
                    "text": "🏚️ PONDOK TUA PENUH MISTERI\n\nDi dalam pondok ono kakek tua bijaksana.\nDheweke ternyata penjaga hutan keramat!\n\n'Mbok menawa kowe pengen harta karun?\nHarta sejati ada dalam dirimu sendiri!'",
                    "choices": [
                        {"text": "🙏 Minta petunjuk spiritual", "next": "good_ending_bijaksana"},
                        {"text": "💸 Tetap minta harta", "next": "bad_ending_materialistis"},
                        {"text": "📝 Tanya sejarah hutan", "next": "secret_ending_penjaga"}
                    ]
                },

                "good_ending_bijaksana": {
                    "text": "🌿 ENDING BAIK: ORANG BIJAKSANA!\n\nKakek ngajarke kowe tentang filosofi hidup Jawa.\nKowe nemu 'harta' dalam kebijaksanaan tradisional.\n\nKowe jadi sesepuh muda yang dihormati masyarakat!\n\n🏆 Pencapaian: Pewaris Kebijaksanaan",
                    "ending": "Orang Bijaksana",
                    "type": "good"
                },

                "gunung_kawasan": {
                    "text": "🏔️ GUNUNG KAWASAN TERJAL\n\nKowe mendaki gunung yang curam.\nPemandangan indah, tapi jalur berbahaya!\n\nTiba-tiba nemu dua jalan:\n- Jalan kiri: Menuju puncak\n- Jalan kanan: Menuju lembah tersembunyi",
                    "choices": [
                        {"text": "⬅️ Jalan kiri ke puncak", "next": "puncak_gunung"},
                        {"text": "➡️ Jalan kanan ke lembah", "next": "lembah_tersembunyi"}
                    ]
                },

                "puncak_gunung": {
                    "text": "⛰️ PUNCAK GUNUNG MEGAH!\n\nDari puncak kowe liat pemandangan spektakuler!\nTernyata 'harta karun' adalah keindahan alam Jawa Timur!\n\nKowe jadi fotografer landscape terkenal!",
                    "ending": "Fotografer Alam",
                    "type": "good"
                },

                "lembah_tersembunyi": {
                    "text": "🪨 LEMBAH TERSEMBUNYI AJAIB!\n\nKowe nemu lembah dengan air terjun dan bunga langka.\nIni adalah tempat meditasi para empu zaman dulu!\n\nKowe nemu kedamaian batin yang tak ternilai!",
                    "ending": "Pencari Kedamaian",
                    "type": "good"
                }
            }
        }

    def create_info_data(self):
        """Data informasi program"""
        return {
            "tentang_program": {
                "nama": "SEBERAPA JATIM SIH KAMU?",
                "deskripsi": "Game CLI interaktif bertema budaya Jawa Timur",
                "teknologi": "Dibuat dengan Python CLI tanpa library eksternal",
                "penyimpanan": "Data disimpen nganggo JSON"
            },
            "developer": [
                "Wisanggeni Cahya Manggalar",
                "Kharis Fatur Rohman"
            ],
            "sekolah": "SMKN 1 DLANGGU",
            "credits": {
                "ai_assistant": "ChatGPT",
                "tema": "Budaya Jawa Timur", 
                "versi": "1.0",
                "tahun": "2025"
            }
        }

    def load_data(self, filename):
        """Load data dari file JSON dengan error handling"""
        try:
            filepath = f"{self.data_dir}/{filename}"
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return {}
                return json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError, ValueError):
            return {}

    def save_data(self, filename, data):
        """Save data ke file JSON"""
        with open(f"{self.data_dir}/{filename}", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def save_user_data(self, user_data):
        """Save data user dengan key berdasarkan nama"""
        current_data = self.load_data("userdata.json")
        username = user_data["nama"]
        current_data[username] = user_data
        self.save_data("userdata.json", current_data)

    def load_user_data(self, username):
        """Load data user berdasarkan nama"""
        data = self.load_data("userdata.json")
        return data.get(username)
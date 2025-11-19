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
        """50 Pertanyaan tentang Jawa Timur dengan jawaban yang variatif"""
        return {
            "pertanyaan": [
                # SEJARAH & TOKOH (10 pertanyaan)
                {
                    "id": 1, "pertanyaan": "Kota mana di Jatim yang dijuluki 'Kota Pahlawan'?",
                    "pilihan": ["Surabaya", "Malang", "Mojokerto", "Kediri"], "jawaban_benar": 0
                },
                {
                    "id": 2, "pertanyaan": "Siapa pahlawan dari Jatim yang terkenal dengan sebutan 'Bung Tomo'?",
                    "pilihan": ["Soekarno", "Sutomo", "Hatta", "Sudirman"], "jawaban_benar": 1
                },
                {
                    "id": 3, "pertanyaan": "Kerajaan Hindu-Buddha terbesar di Jawa Timur adalah?",
                    "pilihan": ["Singasari", "Majapahit", "Kediri", "Kahuripan"], "jawaban_benar": 1
                },
                {
                    "id": 4, "pertanyaan": "Candi peninggalan Majapahit yang terkenal di Trowulan?",
                    "pilihan": ["Candi Borobudur", "Candi Prambanan", "Candi Bajang Ratu", "Candi Sewu"], "jawaban_benar": 2
                },
                {
                    "id": 5, "pertanyaan": "Raja terbesar Kerajaan Majapahit adalah?",
                    "pilihan": ["Raden Wijaya", "Jayanegara", "Hayam Wuruk", "Tribhuwana"], "jawaban_benar": 2
                },
                {
                    "id": 6, "pertanyaan": "Peristiwa 10 November 1945 terjadi di kota?",
                    "pilihan": ["Malang", "Sidoarjo", "Surabaya", "Gresik"], "jawaban_benar": 2
                },
                {
                    "id": 7, "pertanyaan": "Pahlawan nasional dari Blitar yang proklamator kemerdekaan?",
                    "pilihan": ["Hatta", "Sudirman", "Soekarno", "Kartini"], "jawaban_benar": 2
                },
                {
                    "id": 8, "pertanyaan": "Kerajaan sebelum Majapahit yang berpusat di Singosari?",
                    "pilihan": ["Kediri", "Kahuripan", "Singasari", "Jenggala"], "jawaban_benar": 2
                },
                {
                    "id": 9, "pertanyaan": "Bandara Internasional Juanda terletak di?",
                    "pilihan": ["Sidoarjo", "Surabaya", "Malang", "Gresik"], "jawaban_benar": 1
                },
                {
                    "id": 10, "pertanyaan": "Jembatan terpanjang di Indonesia yang menghubungkan Surabaya-Madura?",
                    "pilihan": ["Ampera", "Barito", "Suramadu", "Mahakam"], "jawaban_benar": 2
                },

                # GEOGRAFI & WISATA (15 pertanyaan)
                {
                    "id": 11, "pertanyaan": "Gunung tertinggi di Jawa Timur?",
                    "pilihan": ["Bromo", "Semeru", "Arjuno", "Kelud"], "jawaban_benar": 1
                },
                {
                    "id": 12, "pertanyaan": "Gunung berapi aktif yang terkenal dengan lautan pasirnya?",
                    "pilihan": ["Semeru", "Kelud", "Bromo", "Arjuno"], "jawaban_benar": 2
                },
                {
                    "id": 13, "pertanyaan": "Kawah dengan blue fire yang terkenal di dunia?",
                    "pilihan": ["Kawah Bromo", "Kawah Kelud", "Kawah Ijen", "Kawah Arjuno"], "jawaban_benar": 2
                },
                {
                    "id": 14, "pertanyaan": "Kota di Jatim yang dijuluki 'Kota Apel'?",
                    "pilihan": ["Malang", "Surabaya", "Pasuruan", "Batu"], "jawaban_benar": 3
                },
                {
                    "id": 15, "pertanyaan": "Kota di Jatim yang dijuluki 'Kota Angin'?",
                    "pilihan": ["Situbondo", "Banyuwangi", "Probolinggo", "Lumajang"], "jawaban_benar": 2
                },
                {
                    "id": 16, "pertanyaan": "Kota di Jatim yang dijuluki 'Kota Pisang'?",
                    "pilihan": ["Jember", "Banyuwangi", "Lumajang", "Bondowoso"], "jawaban_benar": 2
                },
                {
                    "id": 17, "pertanyaan": "Kota di Jatim yang dijuluki 'Kota Tape'?",
                    "pilihan": ["Lumajang", "Jember", "Banyuwangi", "Bondowoso"], "jawaban_benar": 3
                },
                {
                    "id": 18, "pertanyaan": "Wisata alam yang terkenal di Kota Batu?",
                    "pilihan": ["Selecta", "Songgoriti", "Jawa Timur Park", "Semua benar"], "jawaban_benar": 3
                },
                {
                    "id": 19, "pertanyaan": "Tempat wisata di Banyuwangi yang ada blue fire?",
                    "pilihan": ["Teluk Hijau", "Plengkung", "Kawah Ijen", "Pulau Merah"], "jawaban_benar": 2
                },
                {
                    "id": 20, "pertanyaan": "Kebun binatang tertua di Asia Tenggara?",
                    "pilihan": ["Ragunan", "Gembira Loka", "Kebun Binatang Surabaya", "Taman Safari"], "jawaban_benar": 2
                },
                {
                    "id": 21, "pertanyaan": "Museum transportasi terbesar di Asia?",
                    "pilihan": ["Museum Kereta Api", "Museum Dirgantara", "Museum Angkut", "Museum Bahari"], "jawaban_benar": 2
                },
                {
                    "id": 22, "pertanyaan": "Pantai yang terkenal di Malang Selatan?",
                    "pilihan": ["Sendang Biru", "Ngliyep", "Balekambang", "Semua benar"], "jawaban_benar": 3
                },
                {
                    "id": 23, "pertanyaan": "Gunung yang menjadi batas Jatim-Jateng?",
                    "pilihan": ["Wilis", "Kelud", "Lawu", "Arjuno"], "jawaban_benar": 2
                },
                {
                    "id": 24, "pertanyaan": "Pulau terbesar di Jatim setelah Pulau Jawa?",
                    "pilihan": ["Bawean", "Kangean", "Madura", "Raas"], "jawaban_benar": 2
                },
                {
                    "id": 25, "pertanyaan": "Taman nasional yang melindungi badak Jawa?",
                    "pilihan": ["Alas Purwo", "Baluran", "Meru Betiri", "Bromo Tengger"], "jawaban_benar": 2
                },

                # KULINER (15 pertanyaan)
                {
                    "id": 26, "pertanyaan": "Makanan khas Jatim yang terbuat dari daging sapi dan kuah hitam?",
                    "pilihan": ["Soto", "Rujak", "Rawon", "Pecel"], "jawaban_benar": 2
                },
                {
                    "id": 27, "pertanyaan": "Makanan khas Jatim 'Rujak Cingur' berasal dari kota?",
                    "pilihan": ["Malang", "Madura", "Banyuwangi", "Surabaya"], "jawaban_benar": 3
                },
                {
                    "id": 28, "pertanyaan": "Makanan khas Surabaya berupa lontong dengan tahu, tauge, dan lentho?",
                    "pilihan": ["Lontong Kikil", "Lontong Opor", "Lontong Balap", "Lontong Sayur"], "jawaban_benar": 2
                },
                {
                    "id": 29, "pertanyaan": "Soto ayam dengan koya khas Lamongan?",
                    "pilihan": ["Soto Madura", "Soto Ayam", "Soto Lamongan", "Soto Betawi"], "jawaban_benar": 2
                },
                {
                    "id": 30, "pertanyaan": "Makanan khas Jatim berupa nasi dengan lauk tahu tek?",
                    "pilihan": ["Nasi Rawon", "Nasi Campur", "Nasi Tumpang", "Nasi Pecel"], "jawaban_benar": 3
                },
                {
                    "id": 31, "pertanyaan": "Sate dengan bumbu kacang khas Madura?",
                    "pilihan": ["Sate Ponorogo", "Sate Kelinci", "Sate Ayam", "Sate Madura"], "jawaban_benar": 3
                },
                {
                    "id": 32, "pertanyaan": "Makanan khas Ponorogo?",
                    "pilihan": ["Gulai Kambing", "Rawon", "Pecel", "Sate Ponorogo"], "jawaban_benar": 3
                },
                {
                    "id": 33, "pertanyaan": "Makanan khas Madiun?",
                    "pilihan": ["Rawon", "Soto", "Rujak", "Pecel Madiun"], "jawaban_benar": 3
                },
                {
                    "id": 34, "pertanyaan": "Makanan khas Kediri?",
                    "pilihan": ["Tahu Gejrot", "Tahu Sumedang", "Tahu Takwa", "Tahu Bulat"], "jawaban_benar": 2
                },
                {
                    "id": 35, "pertanyaan": "Makanan khas Banyuwangi?",
                    "pilihan": ["Rujak Soto", "Pecel Rawon", "Soto Oseng", "Sego Tempong"], "jawaban_benar": 3
                },
                {
                    "id": 36, "pertanyaan": "Makanan khas Bondowoso?",
                    "pilihan": ["Jenang Kudus", "Wingko Babat", "Tape Bondowoso", "Klepon"], "jawaban_benar": 2
                },
                {
                    "id": 37, "pertanyaan": "Minuman khas Jatim dari buah kawista?",
                    "pilihan": ["Wedang Ronde", "Bajigur", "Kopi Joss", "Legin"], "jawaban_benar": 3
                },
                {
                    "id": 38, "pertanyaan": "Minuman khas Jatim dari jahe dan gula merah?",
                    "pilihan": ["Bajigur", "Bandrek", "Wedang Jahe", "Secang"], "jawaban_benar": 2
                },
                {
                    "id": 39, "pertanyaan": "Makanan khas Gresik?",
                    "pilihan": ["Lumpia", "Pastel", "Pudak", "Lemper"], "jawaban_benar": 2
                },
                {
                    "id": 40, "pertanyaan": "Makanan khas Trenggalek?",
                    "pilihan": ["Kupat", "Lemang", "Lemper", "Lontong"], "jawaban_benar": 0
                },

                # BUDAYA & KESENIAN (10 pertanyaan)
                {
                    "id": 41, "pertanyaan": "Kesenian Reog berasal dari daerah mana?",
                    "pilihan": ["Surabaya", "Madura", "Ponorogo", "Banyuwangi"], "jawaban_benar": 2
                },
                {
                    "id": 42, "pertanyaan": "Tari Gandrung berasal dari daerah mana?",
                    "pilihan": ["Surabaya", "Madura", "Kediri", "Banyuwangi"], "jawaban_benar": 3
                },
                {
                    "id": 43, "pertanyaan": "Kesenian Ludruk berasal dari daerah mana?",
                    "pilihan": ["Surabaya", "Lamongan", "Jombang", "Bojonegoro"], "jawaban_benar": 0
                },
                {
                    "id": 44, "pertanyaan": "Tari khas Jatim yang biasanya dibawakan penyambutan tamu?",
                    "pilihan": ["Tari Gandrung", "Tari Ngremo", "Tari Jejer", "Tari Remo"], "jawaban_benar": 3
                },
                {
                    "id": 45, "pertanyaan": "Kesenian Karapan Sapi berasal dari?",
                    "pilihan": ["Surabaya", "Lamongan", "Madura", "Bojonegoro"], "jawaban_benar": 2
                },
                {
                    "id": 46, "pertanyaan": "Upacara adat Suku Tengger di Gunung Bromo?",
                    "pilihan": ["Nyepi", "Galungan", "Yadnya Kasada", "Kuningan"], "jawaban_benar": 2
                },
                {
                    "id": 47, "pertanyaan": "Alat musik tradisional Jawa Timur?",
                    "pilihan": ["Angklung", "Sasando", "Kolintang", "Gamelan"], "jawaban_benar": 3
                },
                {
                    "id": 48, "pertanyaan": "Festival tahunan yang terkenal di Banyuwangi?",
                    "pilihan": ["Festival Reog", "Festival Ludruk", "Festival Kuda Lumping", "Festival Gandrung Sewu"], "jawaban_benar": 3
                },
                {
                    "id": 49, "pertanyaan": "Pakaian adat Jawa Timur?",
                    "pilihan": ["Kebaya", "Batik", "Sarung", "Pesa'an"], "jawaban_benar": 3
                },
                {
                    "id": 50, "pertanyaan": "Rumah adat Jawa Timur?",
                    "pilihan": ["Limasan", "Panggung", "Panjang", "Joglo"], "jawaban_benar": 3
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
        """Data petualangan interaktif yang sudah diperbaiki"""
        return {
            "scenes": {
                # === AWAL PETUALANGAN ===
                "start": {
                    "text": "🌅 PETUALANGAN AREK JATIM 🌅\n\nKamu sedang berjalan-jalan di Trowulan, bekas ibukota Majapahit.\nTiba-tiba kamu menemukan peta kuno yang aneh! 🗺️\nPeta ini menunjukkan jalan menuju harta karun Kerajaan Majapahit!\n\nApa yang akan kamu lakukan?",
                    "choices": [
                        {"text": "🚀 Langsung telusuri peta kuno!", "next": "telusuri_peta"},
                        {"text": "🗣️ Tanya warga sekitar dulu", "next": "tanya_warga"},
                        {"text": "🏛️ Lapor ke museum biar aman", "next": "lapor_museum"}
                    ]
                },

                # === JALUR TELUSURI PETA ===
                "telusuri_peta": {
                    "text": "🛣️ JALUR CEPET: TELUSURI PETA!\n\nKamu nekad mengikuti jalan yang ditunjuk peta.\nTiba-tiba menemukan persimpangan:",
                    "choices": [
                        {"text": "🏞️ Lewat Taman Purbakala", "next": "taman_purbakala"},
                        {"text": "🌲 Lewat Hutan Keramat", "next": "hutan_keramat"},
                        {"text": "🔙 Kembali ke awal", "next": "start"}
                    ]
                },

                "taman_purbakala": {
                    "text": "🏺 TAMAN PURBAKALA MISTERIUS\n\nKamu menemukan taman purbakala yang sepi.\nAda prasasti kuno berisi teka-teki:\n\n'Yang mencari harta tanpa ilmu\nBagai keris tanpa warangka'",
                    "choices": [
                        {"text": "🔍 Periksa prasasti lebih detail", "next": "prasasti_detail"},
                        {"text": "🏃‍♂️ Cepat pergi, serem!", "next": "minggat_serem"}
                    ]
                },

                "prasasti_detail": {
                    "text": "🔎 RAHASIA PRASASTI TERBUKA!\n\nKamu menemukan simbol rahasia di balik prasasti!\nSymbol ini menunjukkan lokasi gua tersembunyi.",
                    "choices": [
                        {"text": "🤝 Jelaskan tujuan mulia", "next": "good_ending_arkeolog"},
                        {"text": "💨 Lari bawa simbol!", "next": "chase_sequence"}
                    ]
                },

                # === JALUR TANYA WARGA ===
                "tanya_warga": {
                    "text": "👥 JALUR WARGA: TANYA PENDUDUK\n\nKamu menemui sesepuh desa yang bijaksana.\nDia bercerita:\n\n'Harta karun Majapahit ini dilindungi ujian: Keberanian, Kebijaksanaan, dan Pengorbanan'",
                    "choices": [
                        {"text": "💪 Terima tantangan!", "next": "tiga_ujian"},
                        {"text": "😰 Takut, urungkan saja", "next": "urungkan_takut"}
                    ]
                },

                "tiga_ujian": {
                    "text": "⚔️ TIGA UJIAN MAJAPAHIT\n\nSesepuh menuntunmu ke tempat ujian:\nUji keberanian di Guha Macan",
                    "choices": [
                        {"text": "🦁 Masuk Guha Macan", "next": "guha_macan"},
                        {"text": "🔙 Kembali", "next": "tanya_warga"}
                    ]
                },

                "guha_macan": {
                    "text": "🦁 GUHA MACAN - UJI KEBERANIAN\n\nKamu menemukan guha gelap.\nDari dalam ada auman macan yang menakutkan!\n\nTapi kamu lihat, ini hanya patung macan mekanik kuno!\nAda tombol rahasia di balik patung...",
                    "choices": [
                        {"text": "🔼 Pencet tombol atas", "next": "secret_ending_macan"},
                        {"text": "🔽 Pencet tombol bawah", "next": "bad_ending_jebakan"}
                    ]
                },

                # === JALUR MUSEUM ===
                "lapor_museum": {
                    "text": "🏛️ JALUR RESMI: LAPOR MUSEUM\n\nKamu ketemu arkeolog muda yang antusias.\nDia senang sekali menemukan peta kuno!\n\n'Tolong bantu analisis peta ini!'",
                    "choices": [
                        {"text": "🤝 Kerjasama ekspedisi", "next": "good_ending_penemu"},
                        {"text": "💼 Minta imbalan dulu", "next": "bad_ending_serakah"}
                    ]
                },

                # === GOOD ENDING ===
                "good_ending_arkeolog": {
                    "text": "🎉 GOOD ENDING: AHLI ARKEOLOG!\n\nPenjaga ternyata arkeolog senior!\nDia kagum dengan ketekunanmu.\n\nKamu diajak kerjasama ekskavasi situs bersejarah.\nNamamu dicatat dalam sejarah arkeologi Indonesia!",
                    "ending": "Ahli Arkeolog Handal",
                    "type": "good"
                },

                "good_ending_penemu": {
                    "text": "🌟 GOOD ENDING: PENEMU SEJATI!\n\nBersama tim arkeolog, kamu menemukan situs purbakala penting!\nTernyata 'harta karun' sejati adalah pengetahuan sejarah.",
                    "ending": "Penemu Situs Bersejarah",
                    "type": "good"
                },

                # === BAD ENDING ===
                "bad_ending_serakah": {
                    "text": "💸 BAD ENDING: SERAKAH!\n\nKamu minta imbalan besar pada arkeolog.\nTernyata dia adalah kolektor barang ilegal!\n\nKamu ditipu dan peta kunomu dijual ke pasar gelap.",
                    "ending": "Kolektor Serakah",
                    "type": "bad"
                },

                "bad_ending_jebakan": {
                    "text": "🚫 BAD ENDING: TERJEBAK!\n\nTombol bawah ternyata memicu jebakan kuno!\nKamu terkunci dalam guha selama 3 hari.\n\nAkhirnya diselamatkan tim penyelamat.",
                    "ending": "Petualang Terjebak",
                    "type": "bad"
                },

                # === SECRET ENDING ===
                "secret_ending_macan": {
                    "text": "🐯 SECRET ENDING: JAGA MACAN!\n\nTombol atas membuka ruang rahasia!\nTernyata 'harta karun' adalah MACAN JATIM LEGENDARY\n yang masih hidup selama 500 tahun!\n\nKamu ditunjuk sebagai penjaga baru macan suci!",
                    "ending": "Penjaga Macan Suci",
                    "type": "secret"
                },

                # === FUNNY ENDING ===
                "minggat_serem": {
                    "text": "😂 FUNNY ENDING: PETUALANG PENAKUT!\n\nTernyata suara itu cuma kucing liar! 😹\nKamu pulang dengan malu...",
                    "ending": "Petualang Penakut",
                    "type": "funny"
                },

                "urungkan_takut": {
                    "text": "😴 FUNNY ENDING: PEMIMPI HARTA KARUN!\n\nKamu pulang, tidur nyenyak.\nMimpi indah tentang harta karun...",
                    "ending": "Pemimpi Harta Karun",
                    "type": "funny"
                },

                "chase_sequence": {
                    "text": "🏃‍♂️ FUNNY ENDING: PELARI CEPAT!\n\nKamu dikejar penjaga taman!\nTapi kamu lebih cepat dan berhasil kabur!\n\nSayangnya simbol rahasia jatuh dan hilang...",
                    "ending": "Pelari Cepat Tapi Ceroboh",
                    "type": "funny"
                },

                "hutan_keramat": {
                    "text": "🌲 HUTAN KERAMAT MISTERIUS\n\nKamu berjalan di hutan yang angker.\nAda suara gemerisik dan bayangan aneh!\n\nTiba-tiba menemukan pondok tua...",
                    "choices": [
                        {"text": "🚪 Masuk ke pondok", "next": "good_ending_bijaksana"},
                        {"text": "🏃‍♂️ Lari ketakutan", "next": "minggat_serem"}
                    ]
                },

                "good_ending_bijaksana": {
                    "text": "🌿 GOOD ENDING: ORANG BIJAKSANA!\n\nKakek tua di pondok mengajarkan filosofi hidup Jawa.\nKamu menemukan 'harta' dalam kebijaksanaan tradisional.\n\nKamu jadi sesepuh muda yang dihormati masyarakat!",
                    "ending": "Orang Bijaksana", 
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
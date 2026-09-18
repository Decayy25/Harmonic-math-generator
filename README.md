# Harmonic Math Generator

Proyek ini membuat soal matematika dalam format audio MP3 berbahasa Indonesia. Setiap file berisi pertanyaan matematika yang dibacakan secara otomatis dan disimpan ke folder output.

## Daftar file

- [general_harmonic.py](general_harmonic.py) — generator soal matematika dasar dengan operasi tambah, kurang, kali, dan bagi.
- [advanced_harmonic.py](advanced_harmonic.py) — generator soal tingkat lanjut dengan operasi tambahan seperti pangkat dua, akar kuadrat, dan pecahan.

## Fitur

- Membuat soal matematika acak secara otomatis
- Menggunakan Google Text-to-Speech (gTTS) untuk mengubah teks menjadi audio
- Menyimpan hasil dalam format MP3
- Mendukung fallback ke pyttsx3 bila gTTS tidak tersedia
- Menghasilkan playlist dengan jumlah soal yang bisa diatur

## Persyaratan

Pastikan Python sudah terinstal di sistem Anda.

Install dependency yang dibutuhkan:

```bash
pip install gTTS
```

Untuk fallback local engine:

```bash
pip install pyttsx3
```

## Cara menjalankan

Jalankan file generator yang diinginkan:

```bash
python general_harmonic.py
```

atau

```bash
python advanced_harmonic.py
```

## Output

Program akan membuat folder berikut:

- `playlist_math` untuk file dari [general_harmonic.py](general_harmonic.py)
- `playlist_math_advanced` untuk file dari [advanced_harmonic.py](advanced_harmonic.py)

Semua file MP3 akan disimpan di dalam folder tersebut.

## Catatan

- Nilai `JUMLAH_FILE` dan `JUMLAH_LANGKAH` dapat diubah di dalam file Python sesuai kebutuhan.
- Koneksi internet diperlukan saat menggunakan gTTS untuk menghasilkan audio dari Google.
- Jika koneksi tidak tersedia, program akan mencoba fallback ke mesin suara lokal.

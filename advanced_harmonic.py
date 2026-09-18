import os
import random
import math

from gtts import gTTS

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None

def is_perfect_square(n):
    if n < 1:
        return False
    r = int(math.isqrt(n))
    return r * r == n

def generate_advanced_math_prompt(num_steps):
    # Mulai dengan angka acak 2 - 15
    current_val = random.randint(2, 15)
    prompt_parts = [f"Soal tingkat lanjut. {current_val}..."]
    script_log = [f"Awal: {current_val}"]

    for _ in range(num_steps):
        ops = ['+']
        if current_val > 1:
            ops.append('-')

        # 1. Perkalian (jika nilai belum terlalu besar)
        if current_val <= 20:
            ops.append('*')

        # 2. Pembagian (hanya jika ada pembagi bulat)
        divisors = [d for d in range(2, 10) if current_val % d == 0 and d != current_val]
        if divisors:
            ops.append('/')

        # 3. Pangkat Dua (hanya jika angka <= 12 agar tidak meledak)
        if current_val <= 12:
            ops.append('pow2')

        # 4. Akar Kuadrat (hanya jika angka saat ini adalah kuadrat sempurna)
        if is_perfect_square(current_val) and current_val > 1:
            ops.append('sqrt')

        # 5. Pecahan (hanya jika habis dibagi penyebut)
        fractions = []
        for den in [2, 3, 4, 5]:
            if current_val % den == 0:
                name = "setengah" if den == 2 else f"seper{den}"
                fractions.append((1, den, name))
                if den == 4 and current_val % 4 == 0:
                    fractions.append((3, 4, "tiga per empat"))
        if fractions:
            ops.append('frac')

        # Pilih operasi secara acak dari yang valid
        chosen_op = random.choice(ops)

        if chosen_op == '+':
            operand = random.randint(1, 20)
            current_val += operand
            prompt_parts.append(f"ditambah {operand}...")
            script_log.append(f"+ {operand} (={current_val})")

        elif chosen_op == '-':
            operand = random.randint(1, min(current_val - 1, 20))
            current_val -= operand
            prompt_parts.append(f"dikurang {operand}...")
            script_log.append(f"- {operand} (={current_val})")

        elif chosen_op == '*':
            operand = random.randint(2, 4)
            current_val *= operand
            prompt_parts.append(f"dikali {operand}...")
            script_log.append(f"× {operand} (={current_val})")

        elif chosen_op == '/':
            operand = random.choice(divisors)
            current_val //= operand
            prompt_parts.append(f"dibagi {operand}...")
            script_log.append(f"÷ {operand} (={current_val})")

        elif chosen_op == 'pow2':
            current_val = current_val ** 2
            prompt_parts.append("dipangkatkan dua...")
            script_log.append(f"^2 (={current_val})")

        elif chosen_op == 'sqrt':
            current_val = int(math.isqrt(current_val))
            prompt_parts.append("diakar kuadratkan...")
            script_log.append(f"√ (={current_val})")

        elif chosen_op == 'frac':
            num, den, text_spoken = random.choice(fractions)
            current_val = (current_val * num) // den
            prompt_parts.append(f"dikali {text_spoken}...")
            script_log.append(f"× {num}/{den} (={current_val})")

    # Jeda hening panjang sebelum jawaban
    prompt_parts.append(f"sama dengan?...... Jawabannya adalah...... {current_val}")

    full_audio_text = " ".join(prompt_parts)
    full_log_text = " -> ".join(script_log)
    return full_audio_text, full_log_text

def save_audio_file(audio_text, file_path):
    try:
        tts = gTTS(text=audio_text, lang='id', slow=False)
        tts.save(file_path)
        return True
    except Exception as exc:
        print(f"  gTTS gagal: {exc}")

    if pyttsx3 is not None:
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.save_to_file(audio_text, file_path)
            engine.runAndWait()
            return True
        except Exception as fallback_exc:
            print(f"  Fallback TTS lokal gagal: {fallback_exc}")

    raise RuntimeError(
        "Tidak bisa membuat MP3. Penyebab biasanya: koneksi internet ke Google Translate tidak tersedia, "
        "atau mesin suara lokal tidak terpasang."
    )

# Konfigurasi Output
JUMLAH_FILE = 10
JUMLAH_LANGKAH = 6
output_folder = "playlist_math_advanced"
os.makedirs(output_folder, exist_ok=True)

print("Membuat playlist Harmonic Math Advanced...\n")

for i in range(1, JUMLAH_FILE + 1):
    audio_text, log_text = generate_advanced_math_prompt(JUMLAH_LANGKAH)
    file_path = os.path.join(output_folder, f"soal_advanced_{i:02d}.mp3")

    save_audio_file(audio_text, file_path)

    print(f"[{i}/{JUMLAH_FILE}] Tersimpan: {file_path}")
    print(f"    Rincian: {log_text}\n")
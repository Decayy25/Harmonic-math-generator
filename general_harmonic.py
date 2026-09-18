import os
import random
from gtts import gTTS

def generate_math_prompt(num_steps):
    current_val = random.randint(2, 20)
    # Tanda titik tiga (...) memberikan jeda hening alami pada audio gTTS
    prompt_parts = [f"Soal. {current_val}..."]
    script_log = [f"Angka awal: {current_val}"]

    for _ in range(num_steps):
        ops = ['+', '-']
        if current_val <= 25:
            ops.append('*')
        
        divisors = [d for d in range(2, 10) if current_val % d == 0 and d != current_val]
        if divisors:
            ops.append('/')

        chosen_op = random.choice(ops)

        if chosen_op == '+':
            operand = random.randint(1, 20)
            current_val += operand
            prompt_parts.append(f"ditambah {operand}...")
            script_log.append(f"+ {operand} (= {current_val})")
        elif chosen_op == '-':
            operand = random.randint(1, min(current_val - 1, 20))
            current_val -= operand
            prompt_parts.append(f"dikurang {operand}...")
            script_log.append(f"- {operand} (= {current_val})")
        elif chosen_op == '*':
            operand = random.randint(2, 5)
            current_val *= operand
            prompt_parts.append(f"dikali {operand}...")
            script_log.append(f"× {operand} (= {current_val})")
        elif chosen_op == '/':
            operand = random.choice(divisors)
            current_val //= operand
            prompt_parts.append(f"dibagi {operand}...")
            script_log.append(f"÷ {operand} (= {current_val})")

    # Jeda sebelum menyebutkan "sama dengan" dan kunci jawaban di akhir audio
    prompt_parts.append("sama dengan?...... Jawabannya adalah...... " + str(current_val))
    
    full_audio_text = " ".join(prompt_parts)
    full_log_text = " -> ".join(script_log) + f" -> HASIL: {current_val}"
    
    return full_audio_text, full_log_text

# Pengaturan Jumlah
JUMLAH_FILE = 10      # Berapa banyak file MP3 yang ingin dibuat
JUMLAH_LANGKAH = 5    # Jumlah operasi per soal

output_folder = "playlist_math"
os.makedirs(output_folder, exist_ok=True)

print("Mulai membuat file MP3...\n")

for i in range(1, JUMLAH_FILE + 1):
    audio_text, log_text = generate_math_prompt(JUMLAH_LANGKAH)
    
    # Generate MP3 via Google TTS (Bahasa Indonesia)
    tts = gTTS(text=audio_text, lang='id', slow=False)
    file_path = os.path.join(output_folder, f"soal_{i:02d}.mp3")
    tts.save(file_path)
    
    print(f"[{i}/{JUMLAH_FILE}] Tersimpan: {file_path}")
    print(f"    Detail: {log_text}\n")

print("Selesai! Semua file MP3 telah tersimpan di folder 'playlist_math'.")
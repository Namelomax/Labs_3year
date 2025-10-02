import random
import string
import json
from pathlib import Path
from datetime import datetime

from crypto_utils import (
    caesar_encrypt, caesar_decrypt,
    vigenere_encrypt, vigenere_decrypt,
    frequency_analysis
)

from text_analyzer import (
    count_words, find_longest_words, calculate_readability_index
)

INPUT_PATH = Path("input.txt")
OUT_DIR = Path("out")
OUT_DIR.mkdir(exist_ok=True)
REPORT_PATH = OUT_DIR / "report.json"
KEYS_PATH = OUT_DIR / "keys.json"


def _save_text(path: Path, text: str):
    path.write_text(text, encoding="utf-8")


def main():
    text = INPUT_PATH.read_text(encoding="utf-8")

    # Генерируем ключ
    caesar_shift = random.randint(1, 25)
    vigenere_key = ''.join(random.choice(string.ascii_letters) for _ in range(6))

    # Шифруем
    caesar_cipher = caesar_encrypt(text, caesar_shift)
    vigenere_cipher = vigenere_encrypt(text, vigenere_key)

    caesar_file = OUT_DIR / f"caesar_{caesar_shift}.txt"
    vigenere_file = OUT_DIR / f"vigenere_{vigenere_key}.txt"

    _save_text(caesar_file, caesar_cipher)
    _save_text(vigenere_file, vigenere_cipher)

    # расшифровка
    decrypted_caesar = caesar_decrypt(caesar_cipher, caesar_shift)
    decrypted_vigenere = vigenere_decrypt(vigenere_cipher, vigenere_key)

    caesar_ok = decrypted_caesar == text
    vigenere_ok = decrypted_vigenere == text

    print("Caesar decrypt OK:", caesar_ok)
    print("Vigenere decrypt OK:", vigenere_ok)

    _save_text(OUT_DIR / f"caesar_decrypted_{caesar_shift}.txt", decrypted_caesar)
    _save_text(OUT_DIR / f"vigenere_decrypted_{vigenere_key}.txt", decrypted_vigenere)

    # Анализ
    report = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "keys": {"caesar": caesar_shift, "vigenere": vigenere_key},
        "stats": {
            "original": {
                "word_count": count_words(text),
                "longest": find_longest_words(text),
                "readability": calculate_readability_index(text)
            },
            "caesar": {
                "word_count": count_words(caesar_cipher),
                "longest": find_longest_words(caesar_cipher),
                "readability": calculate_readability_index(caesar_cipher)
            },
            "vigenere": {
                "word_count": count_words(vigenere_cipher),
                "longest": find_longest_words(vigenere_cipher),
                "readability": calculate_readability_index(vigenere_cipher)
            }
        },
        "freq_analysis": {
            "original": frequency_analysis(text),
            "caesar": frequency_analysis(caesar_cipher),
            "vigenere": frequency_analysis(vigenere_cipher)
        }
    }

    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    KEYS_PATH.write_text(json.dumps({"caesar": caesar_shift, "vigenere": vigenere_key}, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()

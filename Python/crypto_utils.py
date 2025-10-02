import string
from collections import Counter
from typing import Dict

ALPHABET_LOWER = string.ascii_lowercase
ALPHABET_UPPER = string.ascii_uppercase
ALPHABET_LEN = 26

def _shift_char(c: str, shift: int) -> str:
    if c in ALPHABET_LOWER:
        return ALPHABET_LOWER[(ALPHABET_LOWER.index(c) + shift) % len(ALPHABET_LOWER)]
    if c in ALPHABET_UPPER:
        return ALPHABET_UPPER[(ALPHABET_UPPER.index(c) + shift) % len(ALPHABET_UPPER)]
    return c

def caesar_encrypt(text: str, shift: int) -> str:
  return ''.join(_shift_char(c, shift) for c in text)

def caesar_decrypt(text: str, shift: int) -> str:
  return ''.join(_shift_char(c, -shift) for c in text)

def vigenere_encrypt(text: str, key: str) -> str:
  key_shifts = [ALPHABET_LOWER.index(ch.lower()) for ch in key if ch.isalpha()]
  if not key_shifts:
    raise ValueError("Key must contain letters")
  out = []
  ki = 0
  for c in text:
    if c.isalpha():
      shift = key_shifts[ki % len(key_shifts)]
      out.append(_shift_char(c, shift))
      ki += 1
    else:
      out.append(c)
  return ''.join(out)

def vigenere_decrypt(text: str, key: str) -> str:
  key_shifts = [ALPHABET_LOWER.index(ch.lower()) for ch in key if ch.isalpha()]
  if not key_shifts:
    raise ValueError("Key must contain letters")
  out = []
  ki = 0
  for c in text:
    if c.isalpha():
      shift = key_shifts[ki % len(key_shifts)]
      out.append(_shift_char(c, -shift))
      ki += 1
    else:
      out.append(c)
  return ''.join(out)

def frequency_analysis(text: str, only_letters: bool = True) -> Dict[str, int]:
  if only_letters:
    letters = [c.lower() for c in text if c.isalpha()]
  else:
    letters = [c for c in text]
  return dict(Counter(letters))

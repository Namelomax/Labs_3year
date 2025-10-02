import re
from typing import List

_word_re = re.compile(r"\b\w+\b", flags=re.UNICODE)

def count_words(text: str) -> int:
    return len(_word_re.findall(text))

def find_longest_words(text: str, n: int = 5) -> List[str]:
    words = _word_re.findall(text)
    words_sorted = sorted(set(words), key=lambda w: (-len(w), w))
    return words_sorted[:n]

def calculate_readability_index(text: str) -> float:
    words = _word_re.findall(text)
    if not words:
        return 0.0
    avg_len = sum(len(w) for w in words) / len(words)
    return avg_len

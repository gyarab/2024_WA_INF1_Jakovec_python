import os

def load_brainrot_words():
    path = os.path.join(os.path.dirname(__file__), 'brainrot.txt')
    try:
        with open(path, encoding='utf-8') as f:
            return {line.strip().lower() for line in f if line.strip()}
    except FileNotFoundError:
        return set()

BRAINROT_WORDS = load_brainrot_words()

'''
@author jasperan
'''

import os
import sys

# Resolve paths relative to this script's location
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.dirname(_SCRIPT_DIR)

# Matches shorter than this are ignored.
MIN_WORD_LEN = 3


def _read_file(path: str, description: str) -> str:
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        sys.exit(f'Error: {description} not found at {path}')


def _display(s: str) -> str:
    """Render untrusted text inertly: escape C0/C1/DEL control characters (keeps \n, \t)."""
    return ''.join(
        f'\\x{ord(c):02x}' if (ord(c) < 32 and c not in '\n\t') or 127 <= ord(c) < 160 else c
        for c in s
    )


def process_acrostic(word_list: list[str], text: str) -> None:
    sentences = text.split('. ')

    # For each sentence, take the first letter of each word to build the
    # acrostic string, paired with its source sentence.
    extracted = [
        (
            ''.join(w.rstrip()[0] for w in sentence.split(' ') if w.rstrip()),
            sentence,
        )
        for sentence in sentences
    ]
    extracted = [(acrostic.lower(), acrostic, sentence) for acrostic, sentence in extracted]

    # Dictionary hygiene is a property of the words alone, so do it once.
    words = [word for word in word_list if len(word) >= MIN_WORD_LEN]

    for word in words:
        needle = word.lower()
        for acrostic_lower, acrostic, sentence in extracted:
            if needle in acrostic_lower:
                print(
                    f"{_display(word)} -> {_display(acrostic)} "
                    f"||| Full sentence: {_display(sentence)}"
                )


def main() -> None:
    word_list = _read_file(
        os.path.join(_PROJECT_DIR, 'data', 'lemmas_and_words.txt'), 'word list'
    ).splitlines()
    print('Loaded words OK')

    text = _read_file(os.path.join(_PROJECT_DIR, 'data', 'text.txt'), 'input text')
    print('Loaded text OK')

    process_acrostic(word_list, text)


if __name__ == '__main__':
    main()

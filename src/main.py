'''
@author jasperan
'''

import os
import sys

# Resolve paths relative to this script's location
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.dirname(_SCRIPT_DIR)


def _read_file(path: str, description: str) -> str:
	try:
		with open(path, 'r') as f:
			return f.read()
	except FileNotFoundError:
		sys.exit(f'Error: {description} not found at {path}')


def load_words_to_find(path: str) -> list:
	content = _read_file(path, 'word list')
	word_list = [line.rstrip() for line in content.splitlines()]
	print('Loaded words OK')
	return word_list


def load_text_to_analyze(path: str) -> str:
	text = _read_file(path, 'input text')
	print('Loaded text OK')
	return text


def process_acrostic(word_list: list, text: str) -> None:
	sentences = text.split('. ')

	# For each sentence, take the first letter of each word to build the acrostic string
	acrostic_words_extracted = []

	for sentence in sentences:
		sentence_acrostic = ''
		individual_words = sentence.split(' ')
		for word in individual_words:
			if word:
				stripped = word.rstrip()
				if stripped:
					sentence_acrostic += stripped[0]
		acrostic_words_extracted.append(dict(sentence_acrostic=sentence_acrostic, full_sentence=sentence))

	for word in word_list:
		for entry in acrostic_words_extracted:
			acrostic = entry.get('sentence_acrostic')
			if len(word) > 2 and word.lower() in acrostic.lower():
				print(f"{word} -> {acrostic} ||| Full sentence: {entry.get('full_sentence')}")


def main() -> None:
	word_list = load_words_to_find(os.path.join(_PROJECT_DIR, 'data', 'lemmas_and_words.txt'))
	text = load_text_to_analyze(os.path.join(_PROJECT_DIR, 'data', 'text.txt'))
	process_acrostic(word_list, text)


if __name__ == '__main__':
	main()

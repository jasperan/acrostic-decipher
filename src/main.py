'''
@author jasperan
'''

def load_words_to_find(path):
	word_list = list()
	f = open(path, 'r')
	word_list = f.readlines()
	for x in range(len(word_list)):
		word_list[x] = word_list[x].rstrip() # Clean spaces and delimiting characters
	f.close()
	print('Loaded words OK')
	return word_list



def load_text_to_analyze(path):
	text = str()
	f = open(path, 'r')
	text = f.read()
	f.close()
	print('Loaded text OK')
	return text



def process_acrostic(word_list, text):
	sentences = text.split('. ')

	# For all sentences, get the first word
	acrostic_words_extracted = list()

	for x in sentences:
		sentence_acrostic = str()
		individual_words = x.split(' ') # Get the individual words for the sentence
		for y in individual_words:
			if y:
				try:
					sentence_acrostic += y.rstrip()[0]
				except IndexError:
					print('Exception in word {}!'.format(y))
		# print('Acrostic word: {}'.format(sentence_acrostic))
		# Now, we have the acrostic for the sentence. We will try to find coincidences with the words inside them.
		acrostic_words_extracted.append(dict(sentence_acrostic=sentence_acrostic, full_sentence=x))
	for x in word_list:
		for y in acrostic_words_extracted:
			if x.lower() in y.get('sentence_acrostic').lower() and len(x) > 2:
				print('{} -> {} ||| Full sentence: {}'.format(x, y.get('sentence_acrostic'), y.get('full_sentence')))
			else:
				'''print('{} X'.format(y.lower()))'''
				pass




def main():
	word_list = load_words_to_find('../data/lemmas_and_words.txt')
	text = load_text_to_analyze('../data/text.txt')
	result = process_acrostic(word_list, text)



if __name__ == '__main__':
	main()
""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
import pickle
import os.path
from operator import itemgetter

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name,'r')
	lines = f.readlines()
	print(len(lines))
	curr_line = 0
	while lines[curr_line].find("*END*THE SMALL PRINT! FOR PUBLIC DOMAIN ETEXTS*Ver.04.29.93*END*") == -1:
		curr_line += 1
	lines = lines[curr_line+1:]

	lines = [line.strip() for line in lines]
	lines = " ".join(lines)
	lines = "".join([c for c in lines if c.isalpha() or c == " "]) #remove anything but alphabet and space
	words = lines.lower().split()
	return words

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	counter = {}
	for word in word_list:
		if word in counter:
			counter[word] += 1
		else:
			counter[word] = 1

	dictionarychanges = sorted(counter.items(), key = itemgetter(1), reverse = True)
	return dictionarychanges[:n]

if __name__ == '__main__':
	wordlist = get_word_list("DC_Orig_English")
	print(get_top_n_words(wordlist, 10))

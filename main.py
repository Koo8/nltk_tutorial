import pandas as pd
from nltk.book import *

def lexical_diversity(text): # in average, each word type appears how many times
    return len(text)/len(set(text))

def percentage(count, total):
    return 100 * count / total

def find_longwords(text, length, frequency):
    vocub = set(text.split())
    print('the vocularies are ...')
    print(vocub)
    long_words = [w for w in vocub if len(w)> length and FreqDist(text.split())[w] > frequency]
    print(f'longwords are : {long_words}')
    return long_words


'''Produce a dispersion plot of the four main protagonists in Sense and Sensibility(text2):
Elinor, Marianne, Edward, and Willoughby. What can you observe about the
different roles played by the males and females in this novel? Can you identify the
couples?'''
text = '''Notice how we have used two conditions: len(w) > 7 ensures that the words are longer
than seven letters, and fdist5[w] > 7 ensures that these words occur more than seven
times. At last we have managed to automatically identify the frequently occurring content-bearing words of the text. It is a modest but important milestone: a tiny piece of
code, processing tens of thousands of words, produces some informative output'''

fd = FreqDist(text)
# print(fd)
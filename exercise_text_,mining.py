from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import stopwords


# use NLTK’s in-built punkt ***tokeniser*** by calling:
nltk.download('punkt')

humpty_string = "Humpty Dumpty sat on a wall, Humpty Dumpty had a great fall; All the king's horses and all the king's men couldn't put Humpty together again."
humpty_tokens = word_tokenize(humpty_string)
humpty_s_tokens = sent_tokenize(humpty_string)
# Show first 10 entries of the tokens list
# print(humpty_tokens[0:10]) #=>['Humpty', 'Dumpty', 'sat', 'on', 'a', 'wall', ',', 'Humpty', 'Dumpty', 'had']
# print(len(humpty_s_tokens))

english_stopwords = set(stopwords.words('english'))
#  TASK 1: use tokenizer and stopwords to get filted words that's more related  to genre of a corpus
filted_words = [w for w in word_tokenize(humpty_string) if not w in english_stopwords]
# print(filted_words)

# TAKS 2: stemming
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
# find the root for each non-stop words in the tokens
stemmed_roots = [stemmer.stem(w) for w in word_tokenize(humpty_string) if not w in set(stopwords.words('english')) ]
print(stemmed_roots)

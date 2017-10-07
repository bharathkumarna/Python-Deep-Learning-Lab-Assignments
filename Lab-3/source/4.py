from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
import nltk

# Read the file
f = open('datasets/input.txt',"r", encoding="UTF8")

#Tokenize words
sentence = f.read()
tokenized_words = word_tokenize(sentence)
print("Tokenized Words:\n",tokenized_words)

# Remove all the stop words
stop_words = stopwords.words('english')
filter_words = [w for w in tokenized_words if w not in stop_words]
filter_words = [w for w in filter_words if len(w)>2]
print("Filtered words after removing stop words\n",filter_words)

# Using Lemmatization
lemmatized_result = list()
for i in filter_words:
    lemmatized_result.append(WordNetLemmatizer().lemmatize(i))
print("Lemmatized Result\n",lemmatized_result)

# Using POS remove all the verbs
pos_result = list()
for i in pos_tag(lemmatized_result):
    if i[1][:2] == 'VB':
        continue
    else:
        pos_result.append(i[0])
print('POS output after removing verbs\n', pos_result)

# Calculate word frequency of the remaining
words_frequency = nltk.FreqDist(pos_result)
top_fivewords = dict()
for word, frequency in words_frequency.most_common(5):
    top_fivewords[word] = frequency

# Choose top five words
top_fivewords = top_fivewords.keys()
print('Top 5 words\n', top_fivewords)

# Find all the sentences with those most repeated words
output = list()
for lines in sentence.split('\n'):
    for word in top_fivewords:
        if word in lines.lower():
            output.append(lines)
            break

# Extract those sentences and concatenate
print('Summarization\n', "\n".join(output))
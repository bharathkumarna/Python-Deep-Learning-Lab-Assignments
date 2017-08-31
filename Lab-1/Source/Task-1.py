#read input file
inp = open("TextFiles\\input.txt", "r", encoding="UTF8")
#write output file
out = open("TextFiles\\output.txt", "w", encoding="UTF8")

wordcount = {}

#convert text into lowercase and replace new line character ('\n') with space (' ')
text = inp.read().lower().replace('\n', ' ')

#replace non alpha numeric characters with no space charcter ('')
for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
    text = text.replace(ch, '')

#split text file into words by space (' ')
words = text.split(' ')

#loop to count frequency of words
for word in words:
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

#print frequency of words and write output to text file
for k, v in wordcount.items():
    print(k, ':', v)
    print(k, ':', v, file=out)

#close files
inp.close()
out.close()
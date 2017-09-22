inp_string = input("Enter a sentence:")

words_split = inp_string.split()

list_unique = list(set(words_split))

sorted_words = sorted(list_unique, key=str.lower)

output = " ".join(str(x) for x in sorted_words)

print(output)

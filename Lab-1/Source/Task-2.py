import string
#create set with lowercased string
alphabets = set(string.ascii_lowercase)
#input strings
inp = ['How quickly daft jumping zebras vex','How quickly daft jumping zebras']

inp_nospace =[None]*inp.__len__()

for i in range(len(inp)):

    #replace space character (' ') with ('')
    inp_nospace[i] = inp[i].replace(' ', '')

    #check if every letter in the set alphabets is in the set created from input text
    output = ("is not a pangram","is a pangram")[set(inp_nospace[i].lower()) >= alphabets]

    print(inp[i]+' --> '+output)
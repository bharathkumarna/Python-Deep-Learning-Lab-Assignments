import math

inp_no = int(input("Enter a number:"))

list_1 = list(range(1, inp_no+1))
list_2 = []

for x in range(len(list_1)):
    list_2.append(int(math.pow(list_1[x],2)))

dictionary = dict(zip(list_1,list_2))
print(dictionary)
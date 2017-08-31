#declare array
result = []

#loop to find numbers which are divisible by 5 and multiple of 2
for x in range(700, 1700):
    if(x % 7 == 0) and (x % 5 == 0):
        result.append(x)

print(result)
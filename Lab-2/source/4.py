import numpy as np

inp_number = np.random.random(15)

print("Input:\n")
print(inp_number)

inp_number[inp_number.argmax()] = 100

print("Output:\n")
print(inp_number)
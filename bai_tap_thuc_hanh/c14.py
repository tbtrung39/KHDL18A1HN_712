binary_dict = {}

for i in range(1, 101):
    binary_dict[i] = bin(i)[2:]

print(binary_dict)
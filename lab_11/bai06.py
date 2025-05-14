with open('lab_11/bangso.txt', 'w') as f:
    f.write("4\n211 133 180 5\n192 168 1 254\n11 1 11 233\n")
    f.close()

with open('lab_11/bangso.txt', 'r') as f:
    lines = f.readlines()

# a
print("Dong dau tien:", lines[1].strip())
print("Dong thu 33:", lines[3].strip())

# b
print("\nNoi dung toan bo file:")
for line in lines:
    print(line.strip())

# c
matrix = []
for line in lines[1:]:  
    nums = list(map(int, line.strip().split()))
    row = [num if num % 2 == 1 else 0 for num in nums]
    matrix.append(row)

with open('lab_11/ODD.txt', 'w') as f:
    for row in matrix:
        f.write(' '.join(map(str, row)) + '\n')
    f.close()

# d
with open('lab_11/ODD.txt', 'r') as f:
    last_line = f.readlines()[-1]
    print("\nDong cuoicuoi ODD.txt:", last_line.strip())
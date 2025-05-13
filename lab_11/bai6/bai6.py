with open('matrix.txt', 'w') as f:
    f.write('211 133 180 5\n')
    f.write('192 168 1 254\n')
    f.write('11 1 11 233\n')
    f.write('3 5 7 9\n')

print("Đã tạo file matrix.txt mẫu.")

matrix = []
with open('matrix.txt', 'r') as f:
    for line in f:
        row = list(map(int, line.strip().split()))
        matrix.append(row)
print("Dòng 1:", matrix[0])
print("Dòng 3:", matrix[2])

print("\nToàn bộ ma trận:")
for row in matrix:
    print(row)

with open('ODD.txt', 'w') as f:
    for row in matrix:
        new_row = [num if num % 2 != 0 else 0 for num in row]
        f.write(' '.join(map(str, new_row)) + '\n')

print("\nĐã ghi file ODD.txt")
with open('ODD.txt', 'r') as f:
    lines = f.readlines()
    last_line = lines[-1].strip()
    print("\nNội dung dòng cuối ODD.txt:", last_line)
filename = input('Nhập đường dẫn đến file: ')

with open(filename, 'r') as f:
    lines = f.readlines()
    print("Dòng đầu tiên:", lines[0].strip())
    if len(lines) >= 3:  
        print("Dòng thứ 3:", lines[2].strip())
    else:
        print("File không có đủ 3 dòng")

with open(filename, 'r') as f:
    print("\nToàn bộ file:")
    print(f.read())

odd_numbers = []
with open(filename, 'r') as f:
    for line in f:
        try:
            numbers = list(map(int, line.strip().split()))
            odd_numbers.extend([num for num in numbers if num % 2 != 0])
        except ValueError:
            continue 
while len(odd_numbers) < 16:
    odd_numbers.append(0)
odd_matrix = [odd_numbers[i*4:(i+1)*4] for i in range(4)]

with open('ODD.txt', 'w') as f:
    for row in odd_matrix:
        f.write(' '.join(map(str, row)) + '\n')

with open('ODD.txt', 'r') as f:
    lines = f.readlines()
    if lines: 
        print("\nDòng cuối của ODD.txt:", lines[-1].strip())
    else:
        print("\nFile ODD.txt trống")
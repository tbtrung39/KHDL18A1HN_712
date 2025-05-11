filename = input('Nhập đường dẫn đến file: ')

# a. Hiển thị dòng đầu và dòng 3
with open(filename, 'r') as f:
    lines = f.readlines()
    print("Dòng đầu tiên:", lines[0].strip())
    if len(lines) >= 3:  # Kiểm tra xem file có ít nhất 3 dòng không
        print("Dòng thứ 3:", lines[2].strip())
    else:
        print("File không có đủ 3 dòng")

# b. Hiển thị toàn bộ file
with open(filename, 'r') as f:
    print("\nToàn bộ file:")
    print(f.read())

# c. Tìm số lẻ và ghi vào ODD.txt
odd_numbers = []
with open(filename, 'r') as f:
    for line in f:
        try:
            numbers = list(map(int, line.strip().split()))
            odd_numbers.extend([num for num in numbers if num % 2 != 0])
        except ValueError:
            continue  # Bỏ qua các dòng không phải là số

# Định dạng thành ma trận 4x4
while len(odd_numbers) < 16:
    odd_numbers.append(0)
odd_matrix = [odd_numbers[i*4:(i+1)*4] for i in range(4)]

with open('ODD.txt', 'w') as f:
    for row in odd_matrix:
        f.write(' '.join(map(str, row)) + '\n')

# d. In nội dung dòng cuối ODD.txt
with open('ODD.txt', 'r') as f:
    lines = f.readlines()
    if lines:  # Kiểm tra xem file có nội dung không
        print("\nDòng cuối của ODD.txt:", lines[-1].strip())
    else:
        print("\nFile ODD.txt trống")
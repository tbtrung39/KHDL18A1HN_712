def tong_so_le_trong_file(path):
    tong = 0
    with open(path, 'r') as file:
        for line in file:
            numbers = map(int, line.split())
            for num in numbers:
                if num % 2 != 0:
                    tong += num
    return tong
print('')
path=input('nhập đường dẫn đến file nội dung muốn đọc nội dung : path= ')
print("Tổng các số lẻ là:", tong_so_le_trong_file(path))
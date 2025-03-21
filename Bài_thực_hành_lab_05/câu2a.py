s = input('Nhập chuỗi: ')
count = 0
for char in s:
        if not (char.isalpha() or char.isdigit()):
            count += 1
print("Số lượng ký tự đặc biệt:", count)   


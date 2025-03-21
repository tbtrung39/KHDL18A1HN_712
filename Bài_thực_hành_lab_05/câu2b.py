s = input('Nhập chuỗi: ')
count = 0
for char in s:
        
        if not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')):
            count += 1
print("Số lượng ký tự đặc biệt:", count)  
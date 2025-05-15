a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
max_num = max(a, b)
while True:
    if max_num % a == 0 and max_num % b == 0:
        bcnn = max_num
        break
    max_num += 1
print("Bội chung nhỏ nhất là:", bcnn)
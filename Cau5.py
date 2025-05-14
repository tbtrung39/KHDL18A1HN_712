# Câu 5. Phép toán với số nguyên
# a) Nhập hai số nguyên và thực hiện phép chia lấy phần nguyên.
# b) Nhập hai số nguyên và thực hiện phép chia lấy dư.
# c) Tìm số đảo ngược của một số nguyên.

# a)
a = int(input())
b = int(input())
print(a // b)
print()

# b)
a = int(input())
b = int(input())
print(a % b)
print()

# c)
n = int(input())
if n != 0:
    print(int(str(n)[::-1]))
else:
    print("Không thể đảo ngược số 0.")

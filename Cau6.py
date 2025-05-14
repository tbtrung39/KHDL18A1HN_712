# Câu 6. Tính tổng các chữ số
# a) Viết chương trình tính tổng các chữ số của một số nguyên.
# b) Kiểm tra xem tổng các chữ số của một số có chia hết cho 9 không.

# a)
n = int(input())
tong_chu_so = sum(int(digit) for digit in str(abs(n)))
print(tong_chu_so)
print()

# b)
n = int(input())
tong_chu_so = sum(int(digit) for digit in str(abs(n)))
if tong_chu_so % 9 == 0:
    print("Yes")
else:
    print("No")

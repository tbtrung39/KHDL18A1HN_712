# Câu 5. Tính tổng với điều kiện
# a) Tính tổng các số chia hết cho 3 từ 1 đến 100.
# b) Tính tổng các số nguyên tố từ 1 đến 50.
# c) Tính tổng các số có chữ số tận cùng là 5 từ 1 đến 200.

# a)
tong_3 = 0
for i in range(1, 101):
    if i % 3 == 0:
        tong_3 += i
print("Tổng các số chia hết cho 3 từ 1 đến 100 là:", tong_3)
print()

# b) 
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

tong_nguyen_to = 0
for i in range(1, 51):
    if la_so_nguyen_to(i):
        tong_nguyen_to += i
print("Tổng các số nguyên tố từ 1 đến 50 là:", tong_nguyen_to)
print()

# c) 
tong_5 = 0
for i in range(1, 201):
    if i % 10 == 5:
        tong_5 += i
print("Tổng các số có chữ số tận cùng là 5 từ 1 đến 200 là:", tong_5)

# Câu 9. Tính tổng với điều kiện
# a) Tính tổng các số nguyên chia hết cho 3 từ 1 đến 100.
# b) Tính tổng các số nguyên tố từ 1 đến 50.

# a) 
tong_3 = sum(i for i in range(1, 101) if i % 3 == 0)
print(tong_3)
print()

# b) 
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

tong_nguyen_to = sum(i for i in range(1, 51) if la_so_nguyen_to(i))
print(tong_nguyen_to)

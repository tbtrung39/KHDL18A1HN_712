# Câu 1. Câu lệnh if
# a) Kiểm tra xem một số nhập vào có lớn hơn 50 không.
# b) Kiểm tra xem số đó có là số nguyên tố không.
# c) Kiểm tra xem số đó có phải là số chính phương không.

# a.
n = int(input("Nhập một số: "))
if n > 50:
    print("Số lớn hơn 50")
else:
    print("Số không lớn hơn 50")

# b.
n = int(input("Nhập một số: "))
if n < 2:
    print("Không phải số nguyên tố")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Là số nguyên tố")
    else:
        print("Không phải số nguyên tố")

# c.
n = int(input("Nhập một số: "))
can = int(n ** 0.5)
if can * can == n:
    print("Là số chính phương")
else:
    print("Không phải số chính phương")

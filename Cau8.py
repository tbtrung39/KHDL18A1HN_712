# Câu 8. Câu lệnh điều kiện if-else
# a) Nhập một số nguyên và kiểm tra xem nó có chia hết cho 5 và 7 không.
# b) Kiểm tra xem một số có phải là số chính phương không.

# a)
n = int(input("Nhập một số nguyên: "))
if n % 5 == 0 and n % 7 == 0:
    print(f"Số {n} chia hết cho cả 5 và 7.")
else:
    print(f"Số {n} không chia hết cho cả 5 và 7.")
print()

# b)
n = int(input("Nhập một số để kiểm tra xem có phải là số chính phương không: "))
import math
sqrt_n = int(math.sqrt(n))
if sqrt_n * sqrt_n == n:
    print(f"Số {n} là số chính phương.")
else:
    print(f"Số {n} không phải là số chính phương.")

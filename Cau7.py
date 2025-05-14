# Câu 7. Kiểm tra số nguyên tố
# a) Kiểm tra xem một số nhập vào có phải là số nguyên tố không.
# b) In tất cả các số nguyên tố nhỏ hơn 100.

# a)
n = int(input("Nhập một số để kiểm tra: "))
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if la_so_nguyen_to(n):
    print(f"Số {n} là số nguyên tố.")
else:
    print(f"Số {n} không phải là số nguyên tố.")
print()

# b)
print("Các số nguyên tố nhỏ hơn 100 là:")
for i in range(2, 100):
    if la_so_nguyen_to(i):
        print(i, end=" ")

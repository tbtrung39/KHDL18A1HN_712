# Câu 9. 
# Tính toán số học nâng cao
# a)	Viết chương trình tính tổng 1^2 + 2^2 + ... + n^2.
# b)	Tính tổng 1/1 + 1/2 + ... + 1/n với n nhập từ bàn phím.

# a.
n = int(input("Nhập số nguyên dương n: "))
tổng_bình_phương = 0
for i in range(1, n + 1):
    tổng_bình_phương += i ** 2
print("Tổng 1^2 + 2^2 + ... + n^2 là:", tổng_bình_phương)

# b.
n = int(input("Nhập số nguyên dương n: "))
tổng_phân_số = 0
for i in range(1, n + 1):
    tổng_phân_số += 1 / i
print("Tổng 1/1 + 1/2 + ... + 1/n là:", tổng_phân_số)


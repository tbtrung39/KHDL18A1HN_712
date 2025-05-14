# Câu 7. Tính toán với số nguyên lớn
# a) Viết chương trình kiểm tra xem một số nguyên có phải là số hoàn hảo hay không.
# b) Kiểm tra xem một số nguyên có phải là số Armstrong hay không. Biết Số Armstrong 
# (hay còn gọi là số Narcissistic) là số nguyên dương có tính chất đặc biệt: một số a 
# có m chữ số và tổng lũy thừa m các chữ số trong a bằng a.

# a) 
def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

n = int(input())
if la_so_hoan_hao(n):
    print("Số hoàn hảo")
else:
    print("Không phải số hoàn hảo")
print()

# b) 
def la_so_armstrong(n):
    s = str(n)
    m = len(s)
    tong = sum(int(digit) ** m for digit in s)
    return tong == n

n = int(input())
if la_so_armstrong(n):
    print("Số Armstrong")
else:
    print("Không phải số Armstrong")

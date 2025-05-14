# Câu 10. Tính toán với số nguyên
# a) Viết chương trình nhập một số nguyên và tính giai thừa của nó.
# b) Tính tổng các chữ số của một số nguyên.

# a) 
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input())
print(giai_thua(n))
print()

# b) 
n = int(input())
tong_chu_so = sum(int(digit) for digit in str(abs(n)))
print(tong_chu_so)

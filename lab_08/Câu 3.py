#Câu 3:
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập số nguyên dương n: "))
print(f"Các số nguyên tố nhỏ hơn {n}:")
for i in range(2, n):
    if snt(i):
        print(i, end=' ')
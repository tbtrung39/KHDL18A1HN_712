# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Nhập lại số nguyên dương n (n > 0): "))

print(f"Các số nguyên tố nhỏ hơn hoặc bằng {n}:")
for num in range(2, n+1):
    la_nguyen_to = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            la_nguyen_to = False
            break
    if la_nguyen_to:
        print(num, end=" ")
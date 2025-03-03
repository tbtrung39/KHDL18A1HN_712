n = int(input("Nhập số cần phân tích: "))

print(f"Phân tích {n} thành thừa số nguyên tố: ", end="")

for i in range(2, n + 1):
    while n % i == 0: 
        print(i, end=" ")
        n //= i
    if n == 1:
        break 
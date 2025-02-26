n = int(input("Nhập số nguyên dương: "))
while n <= 0:
    n = int(input("Nhập lại số nguyên dương: "))

i = 2
print("Phân tích thừa số nguyên tố:", end=' ')
while n > 1:
    if n % i == 0:
        print(i, end=" ")
        n //= i
    else:
        i += 1

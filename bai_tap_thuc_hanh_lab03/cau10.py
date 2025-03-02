num = int(input("Nhập số nguyên dương để phân tích thừa số nguyên tố: "))
while num <= 0:
    num = int(input("Nhập lại số nguyên dương: "))

i = 2
print(f"Thừa số nguyên tố của {num} là: ", end="")
while num > 1:
    while num % i == 0:
        print(i, end=" ")
        num //= i
    i += 1

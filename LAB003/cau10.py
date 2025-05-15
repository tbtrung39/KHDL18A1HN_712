n = int(input("Nhập số nguyên dương: "))
i = 2
print(f"Phân tích thừa số nguyên tố của {n}: ", end="")

while n > 1:
    if n % i == 0:
        print(i, end=" ")
        n //= i
    else:
        i += 1
else:
    print("\nĐã phân tích xong!")

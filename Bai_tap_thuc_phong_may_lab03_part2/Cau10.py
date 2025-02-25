n = int(input("Nhập một số nguyên dương: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
else:
    print(f"Phân tích thừa số nguyên tố của {n} là:")
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    if count > 0:
        print(f"2^{count}", end=" ")
    for i in range(3, int(n**0.5) + 1, 2):
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            print(f"{i}^{count}", end=" ")
    if n > 2:
        print(f"{n}^1", end=" ")

    print()

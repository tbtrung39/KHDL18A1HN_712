def in_uoc_so(n):
    print(f"Các ước số của {n} là:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

n = int(input("Nhập số nguyên dương n: "))

if n > 0:
    in_uoc_so(n)
else:
    print("Bạn phải nhập một số nguyên dương!")

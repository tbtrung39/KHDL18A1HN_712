import math
n = int(input("Nhập một số nguyên: "))
nguyen_to = True
if n < 2:
    nguyen_to = False
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            nguyen_to = False
            break
if nguyen_to:
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải số nguyên tố.")
    so_nho = 2
    for num in range(n - 1, 1, -1):
        nguyen_to_nho = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                nguyen_to_nho = False
                break
        if nguyen_to_nho:
            so_nho = num
            break
    so_lon = n + 1
    for num in range(n + 1, n + 1000): 
        nguyen_to_lon = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                nguyen_to_lon = False
                break
        if nguyen_to_lon:
            so_lon = num
            break
    if (n - so_nho) <= (so_lon - n):
        print(f"Số nguyên tố gần nhất là: {so_nho}")
    else:
        print(f"Số nguyên tố gần nhất là: {so_lon}")

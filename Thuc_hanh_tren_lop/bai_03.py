# Nhập số nguyên n
n = int(input("Nhập số nguyên: "))
while n <= 0:
    n = int(input("Nhập lại số nguyên (n > 0): "))

# Kiểm tra số nguyên tố
la_nguyen_to = True
if n < 2:
    la_nguyen_to = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_nguyen_to = False
            break

if la_nguyen_to:
    print(f"{n} là số nguyên tố")
else:
    # Tìm số nguyên tố gần nhất
    duoi = n - 1
    tren = n + 1

    # Tìm số nguyên tố nhỏ hơn gần nhất
    while duoi > 1:
        la_nt = True
        for i in range(2, int(duoi**0.5) + 1):
            if duoi % i == 0:
                la_nt = False
                break
        if la_nt:
            print(f"Số nguyên tố gần nhất nhỏ hơn {n} là {duoi}")
            break
        duoi -= 1

    # Tìm số nguyên tố lớn hơn gần nhất
    while True:
        la_nt = True
        for i in range(2, int(tren**0.5) + 1):
            if tren % i == 0:
                la_nt = False
                break
        if la_nt:
            print(f"Số nguyên tố gần nhất lớn hơn {n} là {tren}")
            break
        tren += 1
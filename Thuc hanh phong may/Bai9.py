def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def bai_9():
    n = int(input("Nhập số tự nhiên n: "))
    A = {i for i in range(2, n+1) if n % i == 0 and la_so_nguyen_to(i)}
    B = {i for i in range(2, n) if la_so_nguyen_to(i) and n % i != 0}
    print("Tập hợp A (ước nguyên tố của n):", A)
    print("Tập hợp B (nguyên tố nhỏ hơn n nhưng không là ước):", B)
bai_9()

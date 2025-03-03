def la_so_nguyen_to(n):
    """Kiểm tra xem n có phải là số nguyên tố không."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to_gan_nhat(n):
    """Tìm số nguyên tố gần n nhất."""
    if la_so_nguyen_to(n):
        return n
    
    i = n - 1
    j = n + 1
    while True:
        if la_so_nguyen_to(i):
            return i
        if la_so_nguyen_to(j):
            return j
        i -= 1
        j += 1

# Ví dụ sử dụng
n = 10
if la_so_nguyen_to(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố, số nguyên tố gần nhất là: {tim_so_nguyen_to_gan_nhat(n)}")
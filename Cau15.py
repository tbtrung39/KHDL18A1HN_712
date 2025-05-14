# Câu 15. Tìm số nguyên tố Mersenne M lớn nhất nhỏ hơn một số N nhập vào. Biết số nguyên tố Mersenne M thỏa mãn điều kiện:
# - M là số nguyên tố
# - M = 2^p – 1 với p cũng là số nguyên tố

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_so_mersenne(n):
    p = 2
    max_mersenne = -1
    while True:
        mersenne = 2**p - 1
        if mersenne >= n:
            break
        if la_so_nguyen_to(p) and la_so_nguyen_to(mersenne):
            max_mersenne = mersenne
        p += 1
    return max_mersenne

N = int(input("Nhập số N: "))
result = tim_so_mersenne(N)
if result != -1:
    print(f"Số nguyên tố Mersenne lớn nhất nhỏ hơn {N} là: {result}")
else:
    print(f"Không có số nguyên tố Mersenne nào nhỏ hơn {N}.")

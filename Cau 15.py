# Câu 15. Tìm số nguyên tố Mersenne M lớn nhất nhỏ hơn một số N nhập vào. Biết số nguyên tố Mersenne M thỏa
# mãn điều kiện:
# - M là số nguyên tố
# - M = 2^p – 1 với p cũng là số nguyên tố

import math
def kiem_tra_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def tim_mersenne_lon_nhat(N):
    p = N - 1
    while p > 1:
        if kiem_tra_nguyen_to(p):
            M = 2**p - 1
            if M < N and kiem_tra_nguyen_to(M):
                return M
        p -= 1
    return None
N = int(input("Nhập N: "))
mersenne = tim_mersenne_lon_nhat(N)
if mersenne is None:
    print(f"Không có số nguyên tố Mersenne nào nhỏ hơn {N}.")
else:
    print(f"Số nguyên tố Mersenne lớn nhất nhỏ hơn {N} là {mersenne}.")

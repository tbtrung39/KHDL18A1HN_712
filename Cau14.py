# Câu 14.	Viết chương trình tìm số nguyên tố lớn nhất có dạng 2^p - 1 nhỏ hơn một số N.

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def tim_mersenne_lon_nhat(N):
    max_mersenne = -1
    p = 2

    while True:
        mersenne = 2**p - 1
        if mersenne >= N:
            break
        if la_so_nguyen_to(mersenne):
            max_mersenne = mersenne
        p += 1
    if max_mersenne != -1:
        print(f"Số nguyên tố dạng 2^p - 1 lớn nhất nhỏ hơn {N} là: {max_mersenne}")
    else:
        print(f"Không tìm được số nguyên tố dạng 2^p - 1 nhỏ hơn {N}")
N = int(input("Nhập số N: "))
tim_mersenne_lon_nhat(N)

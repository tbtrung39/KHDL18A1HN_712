def tong_n_so(n, tong, hien_tai=[]):
    if n == 1:
        if tong >= 1:
            print(hien_tai + [tong])
        return

    for i in range(1, tong - n + 2): 
        tong_n_so(n - 1, tong - i, hien_tai + [i])

N = int(input("Nhập tổng N: "))
n = int(input("Nhập số lượng số hạng n: "))
print(f"Tất cả các bộ nghiệm của {N} = x1 + x2 + ... + x{n}:")
tong_n_so(n, N)

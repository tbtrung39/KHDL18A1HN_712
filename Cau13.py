# Câu 13.	Viết thuật toán phân tích một số thành tích của các số nguyên tố khác nhau.

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def phan_tich_nguyen_to_khac_nhau(n):
    goc = n
    danh_sach_ngto = []

    i = 2
    while i * i <= n:
        if n % i == 0:
            if i in danh_sach_ngto:
                print(f"{goc} KHÔNG thể phân tích thành tích các số nguyên tố khác nhau.")
                return
            danh_sach_ngto.append(i)
            n //= i
            if n % i == 0:
                print(f"{goc} KHÔNG thể phân tích thành tích các số nguyên tố khác nhau.")
                return
        else:
            i += 1
    if n > 1:
        if n in danh_sach_ngto:
            print(f"{goc} KHÔNG thể phân tích thành tích các số nguyên tố khác nhau.")
            return
        danh_sach_ngto.append(n)
    print(f"{goc} = ", end="")
    print(" × ".join(str(p) for p in danh_sach_ngto))
so = int(input("Nhập số nguyên dương: "))
phan_tich_nguyen_to_khac_nhau(so)

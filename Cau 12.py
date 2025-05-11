# Câu 12. Viết thuật toán phân tích một số thành tích của các số nguyên tố khác nhau.

def phan_tich_nguyen_to(n):
    i = 2
    phan_tich = []
    
    while i * i <= n:
        while n % i == 0:
            phan_tich.append(i)
            n //= i
        i += 1 
    if n > 1:
        phan_tich.append(n)
    return phan_tich
n = int(input("Nhập một số nguyên: "))
phan_tich = phan_tich_nguyen_to(n)
if len(phan_tich) > 0:
    print(f"Số {n} được phân tích thành: {' * '.join(map(str, phan_tich))}")
else:
    print(f"Số {n} không có ước số nguyên tố.")

def hoan_vi(danh_sach, k=0):
    if k == len(danh_sach):
        print(danh_sach)
    else:
        for i in range(k, len(danh_sach)):
            danh_sach[k], danh_sach[i] = danh_sach[i], danh_sach[k]
            hoan_vi(danh_sach, k + 1)
            danh_sach[k], danh_sach[i] = danh_sach[i], danh_sach[k]  

n = int(input("Nhập số tự nhiên n: "))
danh_sach = list(range(1, n + 1))
hoan_vi(danh_sach)

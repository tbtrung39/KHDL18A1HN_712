def hoan_vi(danh_sach, vi_tri):
    if vi_tri== len(danh_sach):
        print(danh_sach)
    else:
        for i in range(vi_tri,len(danh_sach)):
            danh_sach[vi_tri],danh_sach[i] = danh_sach[i],danh_sach[vi_tri]
            hoan_vi(danh_sach,vi_tri+1)
            danh_sach[vi_tri],danh_sach[i],danh_sach[vi_tri]

n = int(input("Nhập số tự nhiên n : "))
day_so = list(range(1,n +1))
hoan_vi(day_so,0)
def hoan_vi(danh_sach):
    if len(danh_sach) == 1:
        return [danh_sach[:]]
    
    ket_qua = []
    for i in range(len(danh_sach)):
        phan_Tu = danh_sach[i]
        con_lai = danh_sach[:i] +danh_sach[i+1:]
        for hoan_vi_con in hoan_vi(con_lai):
            ket_qua.append([phan_Tu]+hoan_vi_con)
    return ket_qua

def permutation(n):
    day_so = list(range(1,n+1))
    return hoan_vi(day_so)

n = int(input("Nhập số tự nhiên n : "))
cac_hoan_vi = permutation(n)
for hv in cac_hoan_vi:
    print(hv)
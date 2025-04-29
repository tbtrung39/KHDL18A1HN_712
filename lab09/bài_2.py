def ucln(a,b):
    if b == 0 :
        return a
    else:
        return ucln(b,a%b)
    
def ucln_n_so(danh_sach):
    if len(danh_sach) == 1:
        return danh_sach[0]
    else:
        return ucln(danh_sach[0],ucln_n_so(danh_sach[1:]))
    
n = int(input("Nhập só lượng số nguyên : "))

danh_sach_so = []
for i in range(n):
    so = int(input(f"Nhập số thứ {i+1}: "))
    danh_sach_so.append(so)

ket_qua =ucln_n_so(danh_sach_so)
print("Ước chung lớn nhất của các số : ",ket_qua)
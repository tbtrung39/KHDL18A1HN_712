import chuongtrinh
chon=int(input("Chon loai pt (1_Bac nhat, 2_Bac hai)"))
if chon==1:
    a=float(input("Nhap a:"))
    b=float(input("Nhap b:"))
    print("Ket qua: ")
    chuongtrinh.bacnhat(a,b)
if chon==2:
    a=float(input("Nhap a:"))
    b=float(input("Nhap b:"))
    c=float(input("Nhap c:"))
    print("Ket qua: ")
    chuongtrinh.bachai(a,b,c)
    
from doicoso import doicoso1,doicoso2
n=doicoso1.nhap_so_nguyen()
print(f"So vua nhap: {n}")
print(f"Nhi phan: {doicoso1.nhiphan(n)}")
print(f"Bat phan: {doicoso1.batphan(n)}")
print(f'Thap luc phan: {doicoso1.thaplucphan(n)}')

s=input("Nhap chuoi ki tu: ")
s_ok=doicoso2.loc(s)
print(f"Chuoi hop le: {s_ok}")
h=doicoso2.hecoso(s_ok)
if h==-1:
    print("Khong xac dinh duoc he co so!")
else:
    print("Chuoi thuoc he co so: ",h)
    if h==2:
        print(f"Gia tri co so 10: {doicoso2.he_2_sang_10(s_ok)}")
    elif h==8:
        print(f"Gia tri co so 10: {doicoso2.he_8_sang_10(s_ok)}")
    elif h==16:
        print(f"Gia tri co so 10: {doicoso2.he_16_sang_10(s_ok)}")
    else: 
        print("khhong can chuyen doi vi da la co so 10!")
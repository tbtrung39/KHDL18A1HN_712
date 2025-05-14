n=int(input("Nhap so luong tuple: "))
data=[]
for i in range(n):
    ten=input("Nhap ten: ")
    tuoi=int(input("Nhap tuoi: "))
    diem=int(input("Nhap diem: "))
    data.append(ten, tuoi, diem)
data.sort(key=lambda x: (x[0], x[1], x[2]))
print("\n Danh sach sau khi sap xep: ")
for i in data:
    print(i)
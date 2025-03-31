n=int(input("Nhap so luong tuple: "))
data=[]
for i in range(n):
    name=input("Nhap ten: ")
    age=int(input("Nhap tuoi: "))
    score=int(input("Nhap diem: "))
    data.append(name, age, score)
data.sort(key=lambda x: (x[0], x[1], x[2]))
print("\n Danh sach sau khi sap xep: ")
for i in data:
    print(i)
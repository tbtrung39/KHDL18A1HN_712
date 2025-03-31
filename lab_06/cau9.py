a=input("Nhap vao danh sach so nguyen: ")
a=a.split()
for i in range(len(a)):
    a[i] = int(a[i])
for x in a:
    assert x %2 ==0, f"loi: {x} khong phai so chan"
print("Tat ca deu la so chan")
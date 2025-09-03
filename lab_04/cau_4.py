a=int(input('nhap phan so: '))
while True:
    b=int(input('nhap mau so: '))
    if b != 0:
        break
    print("Mẫu số không được bằng 0. Vui lòng nhập lại.")
print(f"Phân số bạn vừa nhập là: {a}/{b}")

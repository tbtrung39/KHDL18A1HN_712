# Cau 4.
tuso = int(input("Nhap tu so: "))
while True:
    mauso = int(input("Nhap mau so: "))
    if mauso != 0:
        break
    print("Mau so khong duoc bang 0. Vui long nhap lai")
print(f"Phan so cua bai la {tuso}/{mauso}")
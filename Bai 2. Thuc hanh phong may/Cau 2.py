# Cau 2. 

def kiem_tra_chuoi(chuoi):
    if not chuoi.isalpha():
        raise ValueError("Loi ky tu !!!")
    for i in range(len(chuoi) - 4):
        if chuoi[i] == chuoi[i+1] == chuoi[i+2] == chuoi[i+3] == chuoi[i+4]:
            raise ValueError("Loi nhap trung lap !!!")
    for i in range(len(chuoi) - 3):
        if chuoi[i] == chuoi[i+1] == chuoi[i+2] == chuoi[i+3]:
            raise ValueError("Loi nhap lap lai !!!")
    for i in range(len(chuoi) - 1):
        if chuoi[i] == chuoi[i+1]:
            raise ValueError("Loi nhap lieu !!!")
    return True
while True:
    try:
        s = input("Nhap chuoi ky tu: ")
        if kiem_tra_chuoi(s):
            print("Chuoi hop le.")
            break
    except ValueError as e:
        print(e)
        print("Moi ban nhap lai.")

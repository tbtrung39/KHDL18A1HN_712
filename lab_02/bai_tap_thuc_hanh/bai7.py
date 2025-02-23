diem = float(input("Nhap diem: "))
if diem>=0.0 and diem<=10.0:
    if diem ==10.0:
        print("hoc sinh dat hoc luc suat xac")
    elif diem >=9.0:
        print("hoc sinh dat hoc luc gioi")
    elif diem >=7.0:
        print("hoc sinh dat hoc luc kha")
    elif diem >=5.0:
        print("hoc sinh dat hoc luc trung binh")
    elif diem >=3.0:
        print("hoc sinh dat hoc luc yeu")
    elif diem <3.0:
        print("hoc sinh dat hoc luc kem")
    else:
        print("du lieu diem sai. Vui long nhap lai")
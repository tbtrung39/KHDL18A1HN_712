# Cau 13.
chuoi = input("Nhap chuoi ki tu: ")
dict_kt = {chuoi[i:i+2]: chuoi.count(chuoi[i:i+2]) for i in range(len(chuoi)-1)}
print("Tu dien 2 ki tu va so lan xuat hien:", dict_kt)
# Câu 15
danh_sach = []
while True:
    du_lieu = input("Nhap thong tin (name, age, score) hoac nhap 'done' de ket thuc: ")
    if du_lieu.lower() == "done":
        break
    try:
        name, age, score = du_lieu.split(",")
        danh_sach.append((name.strip(), int(age.strip()), int(score.strip())))
    except ValueError:
        print("Du lieu khong hop le, vui long nhap lai!")
danh_sach.sort(key=lambda x: (x[0], x[1], x[2]))
print("\nDanh sach sau khi sap xep:")
for item in danh_sach:
    print(item)
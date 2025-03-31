danh_sach = []
while True:
    nhap = input("Nhập thông tin (name, age, score) hoặc Enter để dừng: ")
    if nhap == "":
        break   
    name, age, score = nhap.split(",")
    danh_sach.append((name.strip(), int(age), int(score)))
danh_sach.sort(key=lambda x: (x[0], x[1], x[2]))
print("Danh sách sau khi sắp xếp:")
for item in danh_sach:
    print(item)
n = int(input("Nhập số lượng tuple: "))
danh_sach = []
for _ in range(n):
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    score = float(input("Nhập điểm: "))
    danh_sach.append((name, age, score))
danh_sach.sort(key=lambda x: (x[0], x[1], x[2]))
print("Danh sách sau khi sắp xếp:")
for item in danh_sach:
    print(item)

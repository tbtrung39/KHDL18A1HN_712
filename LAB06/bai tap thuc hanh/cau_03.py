a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
a.sort(key=lambda x: x <= 0)
print("Danh sach sau khi chuyen so duong le dau:", a)
m = int(input("Nhap so m: "))
a.insert(0, m)
a.append(m)
if len(a) >= 5:
    a.insert(4, m)
print("Danh sach sau khi chen m:", a)
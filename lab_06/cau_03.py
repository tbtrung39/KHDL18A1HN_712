
a = []
while True:
    num = int(input("Nhập số tự nhiên (0 để dừng): "))
    if num == 0:
        break
    a.append(num)

a = [x for x in a if x > 0] + [x for x in a if x <= 0]
print("Danh sách sau khi chuyển các số dương lên đầu:", a)

m = int(input("Nhập số m: "))
a = [m] + a + [m]
if len(a) >= 5:
    a.insert(5, m)

print("Danh sách sau khi chèn m:", a)

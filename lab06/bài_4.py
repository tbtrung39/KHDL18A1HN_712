a = []
print("Nhập các số tự nhiên (kết thúc khi nhập 0):")
while True:
    n = int(input("Nhập số: "))
    if n == 0:
        break
    a.append(n)

print("Danh sách ban đầu:", a)

k = int(input("Nhập vị trí phần tử cần xóa (bắt đầu từ 0): "))
if 0 <= k < len(a):
    del a[k]
    print("Danh sách sau khi xóa phần tử thứ", k, ":", a)
else:
    print("Vị trí không hợp lệ.")

m = int(input("Nhập số m cần chèn: "))
a.insert(0, m)
a.append(m)
if len(a) >= 5:
    a.insert(5, m)
else:
    a.append(m)

print("Danh sách sau khi chèn m:", a)

a.sort()
print("Danh sách sau khi sắp xếp tăng dần:", a)
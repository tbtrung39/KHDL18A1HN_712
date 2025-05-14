a = []
while True:
    n = int(input("Nhập một số tự nhiên (nhập 0 để dừng): "))
    if n == 0:
        break
    a.append(n)

i = [1, 2, 3]
a = i + a
a = a + i
if len(a) >= 5:
    a.insert(5, i)
print("Danh sách sau khi chèn [1, 2, 3] vào đầu, cuối và vị trí thứ 5:", a)


K = int(input("Nhập chỉ số K của phần tử muốn xóa: "))
if 0 <= K < len(a):
    a.pop(K)
    print(f"Danh sách sau khi xóa phần tử tại vị trí {K}:")
    print(a)
else:
    print("Chỉ số K không hợp lệ!")


tang = sorted(a)
giam = sorted(a, reverse=True)
print("\nDanh sách sau khi sắp xếp theo thứ tự tăng dần:", tang)
print("\nDanh sách sau khi sắp xếp theo thứ tự giảm dần:", giam)

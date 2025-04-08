nv = {}
n = int(input("Nhập số lượng nhân viên: "))
for _ in range(n):
    ma = input("Mã NV (4 số): ")
    ten = input("Họ tên (tối đa 20 ký tự): ")
    ns = int(input("Năm sinh: "))
    luong = int(input("Lương: "))
    nv[ma] = [ten[:20], ns, luong]

x = input("\nNhập mã cần tìm: ")
if x in nv:
    print("Thông tin nhân viên:", nv[x])
else:
    print("Không tìm thấy mã này.")

y = input("\nNhập mã cần tăng lương: ")
if y in nv:
    nv[y][2] += 1000000
    print("Đã tăng lương cho nhân viên", y)

z = input("\nNhập mã cần xoá: ")
if z in nv:
    del nv[z]
    print("Đã xoá nhân viên", z)

print("\nDanh sách nhân viên theo năm sinh giảm dần:")
ds_sx = sorted(nv.items(), key=lambda x: x[1][1], reverse=True)
for ma, tt in ds_sx:
    print(f"{ma}: {tt}")


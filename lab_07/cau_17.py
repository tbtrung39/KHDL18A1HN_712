n = int(input("Nhập số sinh viên: "))
sv = {}

for _ in range(n):
    ma = input("Mã SV (6 số): ")
    ten = input("Tên: ")
    diem = round(float(input("Điểm: ")))
    sv[ma] = (ten, diem)

ds_sx = sorted(sv.items(), key=lambda x: x[1][1], reverse=True)

print("\nDanh sách sinh viên sắp theo điểm giảm dần:")
for ma, (ten, diem) in ds_sx:
    print(f"{ma} - {ten} - {diem}")

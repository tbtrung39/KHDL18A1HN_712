#Câu 17:
n=int(input("Nhập số sinh viên:"))
ds_sinh_vien=[]
for i in range(n):
    ma_sv=int(input("Nhập mã sinh viên:"))
    ten_sv=input("Nhập tên sinh viên:")
    diem=float(input("Nhập điểm sinh viên:"))
    diem=round(diem)
    ds_sinh_vien.append([ma_sv,ten_sv,diem])
ds_sinh_vien.sort(key=lambda sv: sv[2],reverse=True)
for sv in ds_sinh_vien:
    print(f"{sv[0]}-{sv[1]}-{sv[2]}")

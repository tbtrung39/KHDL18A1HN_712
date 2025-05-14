ds_chieu_cao = [
    161, 182, 161, 154, 176, 170, 167, 171, 170, 174,
    162, 159, 165, 165, 170, 180, 155, 159, 155, 133,
    150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
    152, 162, 180, 168, 169, 188, 161, 167, 170
]

#a
so_luong = len(ds_chieu_cao)
print("Số lượng sinh viên:", so_luong)
#b
trung_binh = sum(ds_chieu_cao) / so_luong
print("Chiều cao trung bình:", round(trung_binh, 2))
#c
chieu_cao = set(ds_chieu_cao)
print("Chiều cao khác nhau:", sorted(chieu_cao))
print("Chiều cao trung bình:", round(sum(ds_chieu_cao) / len(ds_chieu_cao), 2))
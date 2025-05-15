chieu_cao = [
    161, 182, 161, 154, 176, 170, 167, 171, 170, 174,
    150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
    162, 159, 165, 165, 170, 180, 155, 159, 153, 152,
    161, 180, 162, 166, 189, 167, 168, 167, 170
]
so_sinh_vien = len(chieu_cao)
trung_binh = sum(chieu_cao) / so_sinh_vien
chieu_cao_khac_nhau = sorted(set(chieu_cao))
print("Số lượng sinh viên:", so_sinh_vien)
print("Chiều cao trung bình: {:.2f} cm".format(trung_binh))
print("Các chiều cao khác nhau trong nhóm:", chieu_cao_khac_nhau)

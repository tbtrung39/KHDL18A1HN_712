ds_chieu_cao = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174,
                162, 159, 165, 165, 170, 180, 155, 159, 155, 133,
                150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
                152, 162, 180, 168, 169, 188, 161, 167, 170]

# a
so_luong_sv = len(ds_chieu_cao)
print("So luong sinh vien:", so_luong_sv)

# b
trung_binh = sum(ds_chieu_cao) / so_luong_sv
print("Chieu cao trung binh:", round(trung_binh, 2))

# c
tap_chieu_cao = set(ds_chieu_cao)
print("Cac chieu cao khac nhau:", sorted(tap_chieu_cao))
import re
mat_khau_nhap = input("Nhập danh sách mật khẩu (cách nhau bằng dấu phẩy): ").split(',')
mat_khau_hop_le = []
for mat_khau in mat_khau_nhap:
    mat_khau = mat_khau.strip()
    if (6 <= len(mat_khau) <= 12 and
        re.search("[a-z]", mat_khau) and
        re.search("[0-9]", mat_khau) and
        re.search("[A-Z]", mat_khau) and
        re.search("[$#@]", mat_khau)):
        mat_khau_hop_le.append(mat_khau)
print(",".join(mat_khau_hop_le))
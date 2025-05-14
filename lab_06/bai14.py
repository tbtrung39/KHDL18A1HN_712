def kiem_tra_mat_khau(mk: str):
    if len(mk) < 6 or len(mk) > 12:
        return False
    l = [0, 0, 0, 0]
    for c in mk:
        if 'a' <= c <= 'z': l[0] += 1
        elif 'A' <= c <= 'Z': l[1] += 1
        elif c.isdigit(): l[2] += 1
        elif c in '$#@': l[3] += 1
    if l[0] and l[1] and l[2] and l[3]:
        return True
    return False

danh_sach_mat_khau = input("Nhập các mật khẩu cách nhau bởi dấu phẩy: ").split(',')
mat_khau_hop_le = [mk.strip() for mk in danh_sach_mat_khau if kiem_tra_mat_khau(mk.strip())]

if mat_khau_hop_le:
    print("Mật khẩu hợp lệ:", ', '.join(mat_khau_hop_le))
else:
    print("Không có mật khẩu nào hợp lệ")
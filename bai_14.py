import re

def kiem_tra_mat_khau(mat_khau):
    """Kiểm tra tính hợp lệ của mật khẩu theo các tiêu chí."""
    if not 6 <= len(mat_khau) <= 12:
        return False
    if not re.search(r"[a-z]", mat_khau):
        return False
    if not re.search(r"[0-9]", mat_khau):
        return False
    if not re.search(r"[A-Z]", mat_khau):
        return False
    if not re.search(r"[$#@]", mat_khau):
        return False
    return True

if __name__ == "__main__":
    danh_sach_mat_khau = input("Nhập danh sách mật khẩu (phân tách bằng dấu phẩy): ").split(',')
    mat_khau_hop_le = []
    for mk in danh_sach_mat_khau:
        mk = mk.strip()  # Loại bỏ khoảng trắng thừa ở đầu và cuối mỗi mật khẩu
        if kiem_tra_mat_khau(mk):
            mat_khau_hop_le.append(mk)

    if mat_khau_hop_le:
        print(",".join(mat_khau_hop_le))
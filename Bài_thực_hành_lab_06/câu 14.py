import re

def kiem_tra_mat_khau(mat_khau):
    # Kiểm tra độ dài mật khẩu
    if len(mat_khau) < 6 or len(mat_khau) > 12:
        return False
    
    # Kiểm tra ít nhất 1 chữ thường
    if not re.search("[a-z]", mat_khau):
        return False
    
    # Kiểm tra ít nhất 1 chữ hoa
    if not re.search("[A-Z]", mat_khau):
        return False
    
    # Kiểm tra ít nhất 1 chữ số
    if not re.search("[0-9]", mat_khau):
        return False
    
    # Kiểm tra ít nhất 1 ký tự đặc biệt
    if not re.search("[$#@]", mat_khau):
        return False
    
    # Nếu tất cả điều kiện đều thỏa mãn
    return True

# Nhập danh sách mật khẩu cách nhau bởi dấu phẩy
danh_sach_mat_khau = input("Nhập các mật khẩu cách nhau bởi dấu phẩy: ").split(',')

# Kiểm tra từng mật khẩu
mat_khau_hop_le = [mk.strip() for mk in danh_sach_mat_khau if kiem_tra_mat_khau(mk.strip())]

# In kết quả
if mat_khau_hop_le:
    print("Mật khẩu hợp lệ:", ', '.join(mat_khau_hop_le))
else:
    print("Không có mật khẩu nào hợp lệ")
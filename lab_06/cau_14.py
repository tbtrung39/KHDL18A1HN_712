import re
def kiem_tra_mat_khau(mat_khau):
    if len(mat_khau) < 6 or len(mat_khau) > 12:
        return False
    if (re.search(r'[a-z]', mat_khau) and   
        re.search(r'[0-9]', mat_khau) and   
        re.search(r'[A-Z]', mat_khau) and   
        re.search(r'[$#@]', mat_khau)):      
        return True
    return False
mat_khau_input = input("Nhập các mật khẩu phân tách nhau bằng dấu phẩy: ")
mat_khau_list = mat_khau_input.split(',')
mat_khau_hop_le = [mk for mk in mat_khau_list if kiem_tra_mat_khau(mk)]
print(",".join(mat_khau_hop_le))

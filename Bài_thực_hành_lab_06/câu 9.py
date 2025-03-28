danh_sach = list(map(int, input("Nhập danh sách số (cách nhau bằng dấu cách): ").split()))
# Sử dụng assert để kiểm tra
try:
    assert all(so % 2 == 0 for so in danh_sach), "Có số lẻ trong danh sách!"
    print("Tất cả số trong danh sách đều là số chẵn.")
except AssertionError as e:
    print("Lỗi:", e)
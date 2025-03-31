danh_sach = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))
assert all(so % 2 == 0 for so in danh_sach), "Danh sách chứa số lẻ!"
print("Tất cả các số trong danh sách đều là số chẵn.")

danh_sach_1 = [2, 4, 6, 8, 10]
for so in danh_sach_1:
  assert so % 2 == 0, f"Số {so} không phải là số chẵn"
print("Tất cả các số trong danh sách đều là số chẵn.")

danh_sach_2 = [2, 4, 6, 8, 9]
for so in danh_sach_2:
  assert so % 2 == 0, f"Số {so} không phải là số chẵn"
print("Tất cả các số trong danh sách đều là số chẵn.")
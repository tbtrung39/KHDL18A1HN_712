nhat_ky = input("Nhập nhật ký giao dịch: ")
tai_khoan = 0
for i in range(0, len(nhat_ky), 2):
  loai_giao_dich = nhat_ky[i]
  so_tien = int(nhat_ky[i+1])

  if loai_giao_dich == 'D':
    tai_khoan += so_tien
  elif loai_giao_dich == 'W':
    tai_khoan -= so_tien
print("Số tiền trong tài khoản:", tai_khoan)
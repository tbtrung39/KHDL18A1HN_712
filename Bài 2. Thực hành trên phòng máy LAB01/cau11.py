
n = int(input("Nhập số lần tung: "))
xac_suat_ra_6 = 1/216
xac_suat_khong_ra_6 = 1 - xac_suat_ra_6
xac_suat_khong_co_lan_nao_ra_6 = xac_suat_khong_ra_6 ** n
xac_suat_it_nhat_1_lan_ra_6 = 1 - xac_suat_khong_co_lan_nao_ra_6
print(f"Xác suất ít nhất 1 lần cả 3 xúc xắc ra 6 sau {n} lần tung: {xac_suat_it_nhat_1_lan_ra_6:.4f}")

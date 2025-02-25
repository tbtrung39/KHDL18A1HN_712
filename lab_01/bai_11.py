n = int(input("Nhập số lần tung: "))
p_khong_ra = (215 / 216) ** n
xac_suat = 1 - p_khong_ra
print("Xác suất là:%0.2f" % xac_suat)
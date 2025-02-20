#câu11
# Nhập số lần tung xúc sắc n
n = int(input("Nhập số lần tung xúc sắc n: "))
xac_suat_khong_ra_6 = (5 / 6) ** 3
xac_suat = 1 - xac_suat_khong_ra_6 ** n
print(f"Xác suất có ít nhất một lần cả ba xúc sắc ra 6 là: {xac_suat:.2f}")
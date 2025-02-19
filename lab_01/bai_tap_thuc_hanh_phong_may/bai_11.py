import math

n = int(input("Nhập số lần tung xúc xắc: "))

xac_suat_1_lan = (1/6) ** 3
xac_suat_khong_co = (1 - xac_suat_1_lan) ** n
xac_suat_co_it_nhat_1_lan = 1 - xac_suat_khong_co

print(f"Xác suất có ít nhất một lần cả ba xúc xắc ra 6: {xac_suat_co_it_nhat_1_lan:.2f}")

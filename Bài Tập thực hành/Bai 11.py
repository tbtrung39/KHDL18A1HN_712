# Nhập số lần tung xúc xắc
n = int(input("Nhập số lần tung xúc xắc (n): "))

# Tính xác suất
xac_suat_khong_co_3_con_6 = (215/216)**n
xac_suat_co_it_nhat_1_lan_3_con_6 = 1 - xac_suat_khong_co_3_con_6

# Làm tròn đến hai chữ số thập phân
xac_suat_rounded_100 = xac_suat_co_it_nhat_1_lan_3_con_6 * 100
xac_suat_rounded_int = int(xac_suat_rounded_100)
if xac_suat_rounded_100 - xac_suat_rounded_int >= 0.5:
    xac_suat_rounded_int += 1
xac_suat_rounded = xac_suat_rounded_int / 100

# In kết quả
print("Xác suất để có ít nhất 1 lần cả 3 xúc xắc đều ra 6 trong ", end="")
print(n, end="")
print(" lần tung là: ", end="")
print(xac_suat_rounded)

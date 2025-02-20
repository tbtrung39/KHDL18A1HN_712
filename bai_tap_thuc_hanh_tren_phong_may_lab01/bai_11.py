#Tính xác suất
n = int(input("Nhập số lần tung xúc xắc: "))
p = 1 / 216
p_khong_xay_ra = (1 - p) ** n
p_xay_ra_1_lan = 1 - p_khong_xay_ra
print("Xác suất là:", round(p_xay_ra_1_lan, 2))

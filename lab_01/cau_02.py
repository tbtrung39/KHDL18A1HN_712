s=float(input(" xin nhập giá trị giây: ")) 
m=float(input(" xin nhập giá trị phút: "))
h=float(input(" xin nhập giá trị giờ : ")) 
d=float(input(" xin nhập giá trị ngày: "))
tong_gia_tri_giay=(d * 86400) + (h * 3600) + (m * 60) + s 
print(f"Tổng số giây là: {tong_gia_tri_giay} giây") 
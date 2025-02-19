n = int(input("Nhập số lần muốn tung 3 xúc xắc : "))
xac_xuat = int((1 - (215/216)**n )*100)/100
print(f"Xác xuất khi tung {n} lần để có ít nhất 1 lần cả 3 xúc xắc ra 6 là  ",xac_xuat)
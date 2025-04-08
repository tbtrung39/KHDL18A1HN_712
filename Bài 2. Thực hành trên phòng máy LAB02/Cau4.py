so_nguyen = int(input("Nhập vào một số nguyên: "))
so_nguyen = abs(so_nguyen)

if so_nguyen < 100:
    chu_so_hang_tram = 0
else:
    chu_so_hang_tram = (so_nguyen // 100) % 10

print(f"Chữ số hàng trăm của số {so_nguyen} là: {chu_so_hang_tram}")

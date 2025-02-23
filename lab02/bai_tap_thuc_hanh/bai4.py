so_nguyen = int(input("Nhập một số nguyên: "))

if so_nguyen >= 100:
    hang_tram = (so_nguyen // 100) % 10
    print("Chữ số hàng trăm là:", hang_tram)
else:
    print("0")
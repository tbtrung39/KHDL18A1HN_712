def hang_tram(so):
    return (abs(so) // 100) % 10 if abs(so) >= 100 else 0

so = int(input("Nhập vào một số nguyên: "))
print(f"Chữ số hàng trăm của số {so} là: {hang_tram(so)}")

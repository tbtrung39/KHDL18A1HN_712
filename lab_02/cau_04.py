x = int(input("Nhập một số nguyên: "))
if (x) >= 100:
    hang_tram  = (x) // 100 % 10 
    print(f"Chữ số hàng trăm là: {hang_tram}")
else:
    print("Chữ số hàng trăm là: 0")

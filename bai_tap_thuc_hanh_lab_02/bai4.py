so = int(input("Nhập một số nguyên: "))

if abs(so) >= 100:
    print("Chữ số hàng trăm là:", abs(so) // 100 % 10)
else:
    print("Không có chữ số hàng trăm")

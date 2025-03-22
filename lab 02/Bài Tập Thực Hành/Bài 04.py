so = int(input("Nhập số nguyên: "))
if so < 100:
    print("0")
else:
    print(f"Chữ số hàng trăm là: {so // 100 % 10}")
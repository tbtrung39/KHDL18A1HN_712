number = int(input("Nhập vào một số nguyên: "))
if number < 100 and number > -100:
    print(0)
else:
    so_can_tim = (number // 100) % 10
    print("Chữ số hàng trăm là:", abs(so_can_tim))
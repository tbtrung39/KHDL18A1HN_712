sodien = float(input("Nhập số kW điện tiêu thụ: "))

if sodien > 0:
    if sodien > 300:
        print("Số tiền điện cần trả là: ", sodien * 5000)
    elif sodien > 200:
        print("Số tiền điện cần trả là: ", sodien * 3000)
    elif sodien > 100:
        print("Số tiền điện cần trả là: ", sodien * 2500)
    else:
        print("Số tiền điện cần trả là: ", sodien * 2000)
else:
    print("Số điện nhập vào lỗi, vui lòng nhập lại!")

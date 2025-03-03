# Nhập giá trị x từ người dùng
x = float(input("Nhập giá trị của x: "))

# Kiểm tra điều kiện xác định của logarit
if x <= 0 or x == 1:
    print("Biểu thức không xác định.")
else:
    # Tính log4(x)
    log4_x = 0
    temp = 1
    epsilon = 0.000001  # Sai số cho phép

    if x >= 1:
        while temp <= x:
            temp *= 4
            log4_x += 1
        log4_x -=1

        temp /= 4
        diff = x - temp

        while abs(diff/x) > epsilon:
            if temp * 4 <= x:
                temp *=4
                log4_x += 1/(4**(log4_x+1))
            else:
                temp *= (1 + epsilon/10)
                diff = x - temp

    else:
        while temp >= x:
            temp /= 4
            log4_x -= 1
        
        temp *=4
        diff = x - temp

        while abs(diff/x) > epsilon:
            if temp / 4 >= x:
                temp /=4
                log4_x -= 1/(4**(-log4_x+1))
            else:
                temp /= (1 + epsilon/10)
                diff = x - temp
    

    # Tính log4(2) (có thể tính trước giá trị này)
    log4_2 = 0.5

    # Tính giá trị của biểu thức f(x)
    f_x = log4_x + log4_2 / log4_x

    # In kết quả đã làm tròn đến hai chữ số thập phân
    f_x_rounded = int(f_x * 100) / 100

    print("f(x) =", f_x_rounded)
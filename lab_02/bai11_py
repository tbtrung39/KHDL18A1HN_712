ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

if thang in [4, 6, 9, 11] and ngay == 30:
    ngay = 1
    thang += 1
elif thang == 2:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        if ngay == 29:
            ngay = 1
            thang += 1
    else:
        if ngay == 28:
            ngay = 1
            thang += 1
elif thang == 12 and ngay == 31:
    ngay = 1
    thang = 1
    nam += 1
else:
    ngay += 1

print(f"Ngày tiếp theo là: {ngay}/{thang}/{nam}")
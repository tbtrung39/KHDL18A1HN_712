n = int(input("Nhập một số tự nhiên : "))
if n < 0:
    print("Vui lòng nhập số tự nhiên lớn hơn bằng 0")
else:
    nhi_phan=bin(n)[2:]
    print("Biểu diễn nhị phân là: ",nhi_phan)
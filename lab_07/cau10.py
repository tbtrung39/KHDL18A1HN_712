m=int(input("Nhập số tự nhiên m:"))
n=int(input("Nhập số tự nhiên n:"))
digits_m=set(str(m))
digit_n=set(str(n))
common_digits=digits_m & digit_n
total = sum(map(int,common_digits))
print("tổng các chữ số chung:",total)
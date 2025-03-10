num = int(input("Nhập một số nguyên: "))
sum_digits = 0
temp = abs(num)
while temp > 0:
    sum_digits += temp % 10
    temp //= 10
print("Tổng các chữ số của số", num, "là:", sum_digits)

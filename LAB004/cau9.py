num = int(input("Nhập một số nguyên dương: "))
while num < 0:
    num = int(input("Vui lòng nhập số nguyên dương: "))
sum_digits = 0
temp = num

while temp > 0:
    sum_digits += temp % 10
    temp //= 10 
print(f"Tổng các chữ số của {num} là: {sum_digits}")

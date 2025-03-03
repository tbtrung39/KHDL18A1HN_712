num = float(input("Nhập số cần kiểm tra: "))
if num - int(num) >= 0.5:
    rounded_num = int(num) + 1
else:
    rounded_num = int(num)

if num == int(num):
    print(f"{num} là số nguyên.")
else:
    print(f"{num} không phải số nguyên, số nguyên gần nhất là {rounded_num}.")
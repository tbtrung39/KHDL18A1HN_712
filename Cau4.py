# Câu 4. Câu lệnh if-else
# a) Kiểm tra số nhập vào là dương, âm hay bằng 0.
# b) Kiểm tra số nhập vào có phải là bội số của 7 không.
# c) Kiểm tra số nhập vào có phải là số chẵn hay lẻ không.

# a)
n = int(input("Nhập một số: "))
if n > 0:
    print(f"Số {n} là số dương.")
elif n < 0:
    print(f"Số {n} là số âm.")
else:
    print(f"Số {n} bằng 0.")
print()

# b)
if n % 7 == 0:
    print(f"Số {n} là bội số của 7.")
else:
    print(f"Số {n} không phải là bội số của 7.")
print()

# c)
if n % 2 == 0:
    print(f"Số {n} là số chẵn.")
else:
    print(f"Số {n} là số lẻ.")

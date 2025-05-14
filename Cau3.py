# Câu 3. Boolean và logic
# a) Kiểm tra một số nhập vào có lớn hơn 10 không.
# b) Kiểm tra xem số đó có là số chẵn hay không.
# c) Kiểm tra xem số đó có chia hết cho cả 3 và 5 không.

# a)
n = int(input("Nhập một số: "))
if n > 10:
    print(f"Số {n} lớn hơn 10.")
else:
    print(f"Số {n} không lớn hơn 10.")
print()

# b)
if n % 2 == 0:
    print(f"Số {n} là số chẵn.")
else:
    print(f"Số {n} là số lẻ.")
print()

# c)
if n % 3 == 0 and n % 5 == 0:
    print(f"Số {n} chia hết cho cả 3 và 5.")
else:
    print(f"Số {n} không chia hết cho cả 3 và 5.")

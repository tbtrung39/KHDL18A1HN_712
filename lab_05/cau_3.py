n = int(input('nhap so n: '))
binary = ""

if n == 0:
    binary = "0"
else:
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

print("Kết quả hệ nhị phân:", binary)

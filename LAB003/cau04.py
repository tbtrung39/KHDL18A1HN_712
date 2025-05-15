n = int(input("Nhập n: "))
for số in range(2, n + 1):
    for i in range(2, int(số ** 0.5) + 1):
        if số % i == 0:
            break
    else:
        print(số, end=" ")
else:
    print("\nHoàn thành liệt kê số nguyên tố!")

# Câu 3.
# Vòng lặp for
# a) In ra các số từ 1 đến 10.
# b) Tính tổng các số từ 1 đến 100.
# c) In bảng cửu chương của số nhập vào.

# a.
for i in range(1, 11):
    print(i)

# b.
tong = 0
for i in range(1, 101):
    tong += i
print("Tổng các số từ 1 đến 100:", tong)

# c.
so = int(input("Nhập một số: "))
for i in range(1, 11):
    print(f"{so} x {i} = {so * i}")

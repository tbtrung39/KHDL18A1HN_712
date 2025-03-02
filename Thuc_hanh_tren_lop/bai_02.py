# Nhập n
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (n > 0): "))

print("Các số hoàn hảo nhỏ hơn", n, "là:")
for num in range(1, n):
    tong_uoc = 0
    for i in range(1, num):
        if num % i == 0:
            tong_uoc += i  # Tính tổng các ước số của num
    if tong_uoc == num:
        print(num, end=" ")  # In số hoàn hảo
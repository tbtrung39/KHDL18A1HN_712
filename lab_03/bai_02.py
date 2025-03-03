n = int(input("Nhập n: "))

print(f"Các số hoàn hảo nhỏ hơn {n} là:", end=" ")

for i in range(1, n):
    tong_uoc = 0  # Khởi tạo tổng ước của i
    for j in range(1, i):  # Tìm các ước số của i
        if i % j == 0:
            tong_uoc += j

    if tong_uoc == i:  # Nếu tổng ước bằng chính nó => số hoàn hảo
        print(i, end=" ")
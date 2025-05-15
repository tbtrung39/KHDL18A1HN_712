n = int(input("Nhập n: "))
tổng_lập_phương = sum(i ** 3 for i in range(1, n + 1))

for _ in range(1):  # Tạo vòng lặp để dùng `else`
    print(f"Tổng bậc 3 của {n} số đầu tiên: {tổng_lập_phương}")
else:
    print("Đã tính xong tổng!")

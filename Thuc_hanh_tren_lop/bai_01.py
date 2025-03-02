# Nhập n
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (n > 0): "))

tong = 1  # Bắt đầu với 1
tich = 1  # Biến tích khởi tạo là 1

for i in range(1, n+1):
    phan_so = (2 * i) / (2 * i + 1)  # Tính giá trị của phân số
    tich *= phan_so  # Nhân dồn vào tích
    tong += tich  # Cộng vào tổng

# In kết quả với 3 chữ số thập phân
print(f"Kết quả của biểu thức là: {tong:.3f}")
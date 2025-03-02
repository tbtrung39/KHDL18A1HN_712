# Nhập chiều cao và chiều rộng của hình chữ nhật
chieu_cao = int(input("Nhập số hàng: "))
chieu_rong = int(input("Nhập số cột: "))

# In hình chữ nhật
for i in range(chieu_cao):
    print("* " * chieu_rong)
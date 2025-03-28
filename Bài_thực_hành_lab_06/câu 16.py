X = int(input("Nhập số hàng X: "))
Y = int(input("Nhập số cột Y: "))

# Tạo mảng 2 chiều sử dụng list comprehension
matrix = [[i * j for j in range(Y)] for i in range(X)]
print("Mảng 2 chiều kết quả:")
for row in matrix:
    print(row)
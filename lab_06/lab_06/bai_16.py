# Câu 16
X = int(input("Nhap X: "))
Y = int(input("Nhap Y: "))
mang = [[i * j for j in range(Y)] for i in range(X)]
print(mang)
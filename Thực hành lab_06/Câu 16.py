#Câu 16:
X = int(input("Nhập X: "))
Y = int(input("Nhập Y: "))

ma_tran = []
for i in range(X):
  hang = []
  for j in range(Y):
    hang.append(i * j)
  ma_tran.append(hang)

print(ma_tran)
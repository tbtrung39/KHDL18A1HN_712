X = int(input("Nhập X: "))
Y = int(input("Nhập Y: "))

m = []
for i in range(X):
  hang = []
  for j in range(Y):
    hang.append(i * j)
  m.append(hang)

print(m)
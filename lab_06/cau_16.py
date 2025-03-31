X = int(input("Nhập số hàng (X): "))
Y = int(input("Nhập số cột (Y): "))
mang = []
for i in range(X):
    hang = [] 
    for j in range(Y):
        hang.append(i * j) 
    mang.append(hang)  
print("Mảng 2 chiều là:")
for hang in mang:
    print(hang)

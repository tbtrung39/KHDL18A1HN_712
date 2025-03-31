m = int(input("Nhập số hàng (m) của ma trận: "))
n = int(input("Nhập số cột (n) của ma trận: "))
A = []
for i in range(m):
    hang = []
    print(f"Nhập các phần tử cho hàng {i+1}:")
    for j in range(n):
        aij = int(input(f"Nhập phần tử a[{i+1}][{j+1}]: "))
        hang.append(aij)
    A.append(hang)
tong = 0
for i in range(m):
    for j in range(n):
        tong += A[i][j]
print("\nMa trận A là:")
for hang in A:
    print(hang)

print(f"Tổng các phần tử của ma trận A là: {tong}")

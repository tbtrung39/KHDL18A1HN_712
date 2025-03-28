# a. nhập ma trân A
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
A = []

for i in range(m):
    row = []
    for j in range(n):
        a_ij = int(input(f"Nhập phần tử A[{i+1}][{j+1}]: "))
        row.append(a_ij)
    A.append(row)

print("\nMa trận A vừa nhập:")
for row in A:
    print(row)

# b. Tính tổng các phần tử ma trận
total = sum(sum(row) for row in A)
print(f"\nTổng các phần tử của ma trận: {total}")
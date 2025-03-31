m, n = map(int, input("Nhập số hàng m và số cột n (cách nhau bằng dấu cách): ").split())

A = []
for i in range(m):
    row = list(map(int, input(f"Nhập các phần tử của hàng {i+1}: ").split()))
    A.append(row)

total_sum = sum(sum(row) for row in A)

print("Tổng các phần tử của ma trận A là:", total_sum)
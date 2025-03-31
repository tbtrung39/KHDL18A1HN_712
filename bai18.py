
m = int(input("Nhập số hàng của ma trận (m): "))
n = int(input("Nhập số cột của ma trận (n): "))

A = []


print("Nhập các phần tử của ma trận (mỗi hàng nhập các phần tử cách nhau bằng khoảng trắng):")
for i in range(m):
    row = list(map(int, input(f"Nhập phần tử cho hàng {i+1}: ").split()))
    while len(row) != n: 
        print(f"Lỗi! Bạn phải nhập đúng {n} phần tử.")
        row = list(map(int, input(f"Nhập lại phần tử cho hàng {i+1}: ").split()))
    A.append(row)


print("\nMa trận A vừa nhập:")
for row in A:
    print(row)

# b
tong = sum(sum(row) for row in A)

print("\nTổng các phần tử của ma trận A là:", tong)

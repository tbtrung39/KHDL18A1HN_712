a = int(input("Nhập số phần tử: "))
n = [int(input(f"Nhập số thứ {i+1}: ")) for i in range(a)]
print("Danh sách:", n)
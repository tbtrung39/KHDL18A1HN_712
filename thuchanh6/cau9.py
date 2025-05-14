n = int(input("Nhập số lượng phần tử trong danh sách: "))
numbers = [int(input(f"Nhập số thứ {i+1}: ")) for i in range(n)]

assert all(num % 2 == 0 for num in numbers), "Không phải tất cả các số đều là số chẵn"
print("Tất cả các số trong danh sách đều là số chẵn.")

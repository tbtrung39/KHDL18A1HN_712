# Bai 9
numbers = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))

assert all(num % 2 == 0 for num in numbers), "Danh sách chứa số lẻ!"

print("Tất cả các số trong danh sách đều là số chẵn.")

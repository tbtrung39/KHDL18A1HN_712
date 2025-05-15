# Câu 9
numbers = list(map(int, input("Nhap cac so nguyen, cach nhau boi dau cach: ").split()))  
assert all(num % 2 == 0 for num in numbers), "Danh sach chua so le!"  
print("Danh sach hop le, tat ca cac so deu la so chan:", numbers)
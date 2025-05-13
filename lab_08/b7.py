numbers = []
for i in range(5):
    num = int(input(f"Nhap số thứ {i+1}: "))
    numbers.append(num)
print("Số nhỏ nhất là: ", min(numbers))
print("Số lớn nhất là: ", max(numbers))
# bai15
n = int(input("Nhập số lượng tuple: "))
tuples = []

for i in range(n):
    name = input(f"Nhập tên của phần tử thứ {i + 1}: ")
    age = int(input(f"Nhập tuổi của phần tử thứ {i + 1}: "))
    score = float(input(f"Nhập điểm của phần tử thứ {i + 1}: "))
    tuples.append((name, age, score))

tuples.sort(key=lambda x: (x[0], x[1], x[2]))

print("\nDanh sách sau khi sắp xếp:")
for tup in tuples:
    print(tup)

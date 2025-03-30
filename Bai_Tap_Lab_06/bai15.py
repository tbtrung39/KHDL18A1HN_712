data = []
while True:
    user_input = input("Nhập tuple (name, age, score) hoặc nhấn Enter để kết thúc: ")
    if not user_input:
        break
    parts = user_input.split(',')
    name = parts[0].strip()
    age = int(parts[1].strip())
    score = int(parts[2].strip())
    data.append((name, age, score))

sorted_data = sorted(data, key=lambda x: (x[0], x[1], x[2]))
print("\nDanh sách sau khi sắp xếp:")
for item in sorted_data:
    print(item)
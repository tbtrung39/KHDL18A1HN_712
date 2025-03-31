import random
lst4 = [random.randint(1, 99999) for _ in range(1000)]
print("Danh sách ban đầu:", lst4[:10], "...")  # In 10 phần tử đầu
lst4_sorted = sorted(lst4)
print("Danh sách sau khi sắp xếp (sorted()):", lst4_sorted[:10], "...")

# Sắp xếp không dùng sorted()
for i in range(len(lst4)):
    for j in range(i + 1, len(lst4)):
        if lst4[i] > lst4[j]:
            lst4[i], lst4[j] = lst4[j], lst4[i]
print("Danh sách sau khi sắp xếp (thuật toán đổi chỗ):", lst4[:10], "...")
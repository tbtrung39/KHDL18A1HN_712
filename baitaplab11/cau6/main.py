# Tạo và ghi dữ liệu vào file dữ liệu gốc
with open("data.txt", "w") as f:
    f.write("211 133 180 5\n")
    f.write("192 168 1 254\n")
    f.write("11 1 11 233\n")

# a. Hiển thị dòng đầu và dòng thứ 3
with open("data.txt", "r") as f:
    lines = f.readlines()
    print("Dòng đầu:", lines[0].strip())
    print("Dòng thứ 3:", lines[2].strip())

# b. Hiển thị toàn bộ nội dung file
print("\nToàn bộ nội dung file:")
with open("data.txt", "r") as f:
    print(f.read())

# c. Ghi các số lẻ thành ma trận 4x4 vào ODD.txt (số chẵn -> 0)
# Đọc toàn bộ số từ file
so_le = []
with open("data.txt", "r") as f:
    for line in f:
        numbers = map(int, line.strip().split())
        for n in numbers:
            so_le.append(n if n % 2 == 1 else 0)

# Bổ sung thêm số 0 nếu chưa đủ 16 phần tử
while len(so_le) < 16:
    so_le.append(0)

# Ghi thành ma trận 4x4
with open("ODD.txt", "w") as f:
    for i in range(4):
        dong = so_le[i*4:(i+1)*4]
        f.write(" ".join(map(str, dong)) + "\n")

# d. In ra nội dung dòng cuối của ODD.txt
with open("ODD.txt", "r") as f:
    lines = f.readlines()
    print("\nDòng cuối của ODD.txt:")
    print(lines[-1].strip())
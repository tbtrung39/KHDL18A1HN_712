# === Ghi file đầu vào ===
with open("input_matrix.txt", "w") as f:
    f.write("4\n")
    f.write("211 133 180 5\n")
    f.write("192 168 1 254\n")
    f.write("11 1 11 233\n")

# === Đọc nội dung từ file ===
def doc_file(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

# === a. Hiển thị dòng đầu tiên và dòng thứ 3 ===
def hien_thi_dong_1_va_3(lines):
    print("Dòng đầu tiên:", lines[0])
    if len(lines) >= 3:
        print("Dòng thứ 3:", lines[2])

# === b. Hiển thị toàn bộ file ===
def hien_thi_toan_bo(lines):
    print("\nToàn bộ nội dung file:")
    for line in lines:
        print(line)

# === c. Ghi các số lẻ ra file ODD.txt dưới dạng ma trận 4x4 ===
def ghi_ma_tran_odd(lines, filename_out):
    matrix = []
    for line in lines[1:]:
        row = list(map(int, line.split()))
        matrix.append(row)
    odd_matrix = [[0]*4 for _ in range(4)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 2 == 1:
                odd_matrix[i][j] = matrix[i][j]
    with open(filename_out, "w") as f:
        for row in odd_matrix:
            f.write(" ".join(map(str, row)) + "\n")
def in_dong_cuoi_odd(filename_out):
    with open(filename_out, "r") as f:
        lines = f.readlines()
        if lines:
            print("\nDòng cuối cùng trong ODD.txt:")
            print(lines[-1].strip())
du_lieu = doc_file("input_matrix.txt")

# a
hien_thi_dong_1_va_3(du_lieu)

# b
hien_thi_toan_bo(du_lieu)

# c
ghi_ma_tran_odd(du_lieu, "ODD.txt")

# d
in_dong_cuoi_odd("ODD.txt")

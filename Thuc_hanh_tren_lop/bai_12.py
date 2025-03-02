# Bảng giá trị của các chữ cái theo tiêu chuẩn container
values = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, 'J':19,
          'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29,
          'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}

# Nhập mã container (10 ký tự)
container_code = input("Nhập mã container (10 ký tự): ").upper()
while len(container_code) != 10:
    container_code = input("Nhập lại mã container (10 ký tự): ").upper()

# Tính tổng có trọng số
total = 0
for i in range(len(container_code)):
    if container_code[i].isalpha():
        value = values[container_code[i]]  # Giá trị của chữ cái
    else:
        value = int(container_code[i])  # Giá trị số
    total += value * (2 ** i)  # Nhân với 2^i

# Tính số kiểm tra
check_digit = total % 11

# In kết quả
print(f"Số kiểm tra của container {container_code}: {check_digit}")
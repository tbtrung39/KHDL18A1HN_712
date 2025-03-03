# Bảng mã hóa chữ cái thành số
char_to_value = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
    'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29,
    'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}

# Nhập mã container từ người dùng
container_code = input("Nhập mã container (10 ký tự): ").upper()

# Khởi tạo tổng trọng số
total_weight = 0
i = 0  # Vị trí của ký tự

# Xử lý từng ký tự trong container_code
while i < len(container_code):
    char = container_code[i]
    
    # Nếu là chữ cái, lấy giá trị từ bảng mã, nếu là số thì giữ nguyên
    if char.isalpha():
        value = char_to_value[char]
    else:
        value = int(char)
    
    # Nhân với 2^i (vị trí bắt đầu từ 0)
    total_weight += value * (2 ** i)
    
    i += 1  # Tăng vị trí lên 1

# Tính số kiểm tra
check_digit = total_weight % 11

# Xuất kết quả
print("Số kiểm tra của container", container_code, "là:", check_digit)

char_to_value = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20, 
    'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29, 'S': 30, 'T': 31, 
    'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}

def tinh_so_kiem_tra(container):
    if len(container) != 10:
        raise ValueError("Chuỗi container phải có 10 ký tự")
    
    tong_trong_so = 0
    for i in range(10):
        char = container[i]
        
        if i < 4:
            value = char_to_value.get(char)
            if value is None:
                raise ValueError("Ký tự không hợp lệ trong phần đầu của container")
        else:
            value = int(char)
        
        tong_trong_so += value * (2 ** i)
    
    check_digit = tong_trong_so % 11
    return check_digit
container = input("Nhập số container (10 ký tự): ").strip()

check_digit = tinh_so_kiem_tra(container)
print(f"Số kiểm tra của container là: {check_digit}")
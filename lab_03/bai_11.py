def ve_tam_giac_rong(n, loai):
    """Vẽ tam giác sao rỗng."""
    if n <= 0:
        return "n phải là số nguyên dương"
    
    if loai == 'a':
        for i in range(n):
            if i == 0:
                print("*")
            elif i == n - 1:
                print("* " * n)
            else:
                print("*", "  " * (i - 1), "*")
    elif loai == 'b':
        for i in range(n):
            if i == 0:
                print("*")
            elif i == n - 1:
                print("* " * n)
            else:
                print("*", " " * (i * 2 - 1), "*")
    elif loai == 'c':
        for i in range(n):
            if i == 0:
                print("*")
            else:
                print("*", " " * (i - 1), "*")
    else:
        return "Loại tam giác không hợp lệ"

# Ví dụ sử dụng
ve_tam_giac_rong(5, 'a')
ve_tam_giac_rong(5, 'b')
ve_tam_giac_rong(5, 'c')
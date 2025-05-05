import math

# Tính chu vi hình tròn
def get_ChuVi(r):
    return 2 * r * math.pi  # Sử dụng math.pi thay cho 3.14

# Tính diện tích hình tròn
def get_DienTich(r):
    return math.pi * r * r

# Kiểm tra xem điểm A có nằm trong hình tròn không
def is_In(O, A, r):
    x0, y0 = O
    x, y = A
    if math.sqrt((x0 - x)**2 + (y0 - y)**2) < r:
        return True
    else:
        return False

# Kiểm tra xem điểm A có nằm ngoài hình tròn không
def is_Out(O, A, r):
    x0, y0 = O
    x, y = A
    if math.sqrt((x0 - x)**2 + (y0 - y)**2) > r:
        return True
    else:
        return False

# Kiểm tra xem điểm A có nằm trên hình tròn không
def is_On(O, A, r):
    x0, y0 = O
    x, y = A
    if math.isclose(math.sqrt((x0 - x)**2 + (y0 - y)**2), r, abs_tol=1e-9):
        return True
    else:
        return False

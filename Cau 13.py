# Câu 13. Xác định xem một số có thể biểu diễn dưới dạng tổng của hai số chính phương hay không.

import math
def kiem_tra_tong_chinh_phuong(n):
    for a in range(int(math.sqrt(n)) + 1):
        b = math.sqrt(n - a * a)
        if b.is_integer():
            return True
    return False
n = int(input("Nhập một số nguyên: "))
if kiem_tra_tong_chinh_phuong(n):
    print(f"Số {n} có thể biểu diễn dưới dạng tổng của hai số chính phương.")
else:
    print(f"Số {n} không thể biểu diễn dưới dạng tổng của hai số chính phương.")

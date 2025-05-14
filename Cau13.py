# Câu 13. Viết chương trình kiểm tra xem một số có thể biểu diễn dưới dạng tổng của hai số nguyên tố hay không.

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def kiem_tra_tong_s2nguyen_to(n):
    for i in range(2, n):
        if la_so_nguyen_to(i) and la_so_nguyen_to(n - i):
            return True
    return False
n = int(input("Nhập một số: "))
if kiem_tra_tong_s2nguyen_to(n):
    print(f"Số {n} có thể biểu diễn dưới dạng tổng của hai số nguyên tố.")
else:
    print(f"Số {n} không thể biểu diễn dưới dạng tổng của hai số nguyên tố.")

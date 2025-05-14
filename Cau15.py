# Câu 15.	Xác định xem một số có thể biểu diễn dưới dạng tổng của hai số chính phương hay không.

def la_so_chinh_phuong(n):
    can = int(n**0.5)
    return can * can == n

def co_la_tong_hai_chinh_phuong(n):
    for a in range(int(n**0.5) + 1):
        b_binh = n - a*a
        if b_binh >= 0 and la_so_chinh_phuong(b_binh):
            b = int(b_binh**0.5)
            print(f"{n} = {a}^2 + {b}^2")
            return True
    return False

n = int(input("Nhập số nguyên dương: "))
if not co_la_tong_hai_chinh_phuong(n):
    print(f"{n} không thể biểu diễn thành tổng của hai số chính phương.")

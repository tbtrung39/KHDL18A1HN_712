# Câu 12.	Viết chương trình kiểm tra xem một số nguyên có thể viết được dưới dạng tổng của ba số nguyên tố hay không.

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập số nguyên cần kiểm tra: "))
tim_duoc = False
for a in range(2, n):
    if la_so_nguyen_to(a):
        for b in range(a, n): 
            if la_so_nguyen_to(b):
                c = n - a - b
                if c >= b and la_so_nguyen_to(c):  
                    print(f"{n} = {a} + {b} + {c}")
                    tim_duoc = True
                    break
        if tim_duoc:
            break

if not tim_duoc:
    print(f"{n} KHÔNG thể viết thành tổng của ba số nguyên tố.")

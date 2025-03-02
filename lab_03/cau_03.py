def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False 
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False 
    return True
def so_nguyen_to_gan_nhat(n):
    so_nguyen_to_nho = n - 1
    while so_nguyen_to_nho >= 2:
        if kiem_tra_so_nguyen_to(so_nguyen_to_nho):
            break
        so_nguyen_to_nho -= 1
    so_nguyen_to_lon = n + 1
    while True:
        if kiem_tra_so_nguyen_to(so_nguyen_to_lon):
            break
        so_nguyen_to_lon += 1
    if n - so_nguyen_to_nho <= so_nguyen_to_lon - n:
        return so_nguyen_to_nho
    else:
        return so_nguyen_to_lon
n = int(input("Nhập vào số n: "))
if kiem_tra_so_nguyen_to(n):
    print(f"{n} là số nguyên tố.")
else:
    gan_nhat = so_nguyen_to_gan_nhat(n)
    print(f"{n} không phải là số nguyên tố. Số nguyên tố gần nhất là {gan_nhat}.")

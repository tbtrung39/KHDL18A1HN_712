def so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def dem_so_nguyen_to(lst):
    return [x for x in lst if so_nguyen_to(x)]

lst = list(map(int, input("Nhập danh sách số nguyên: ").split()))
print("Các số nguyên tố:", dem_so_nguyen_to(lst))
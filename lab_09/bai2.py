def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)

def ucln_list(i, n, result):
    if i == n:
        return result
    x = int(input(f"Nhập số thứ {i+1}: "))
    return ucln_list(i+1, n, ucln(result, x))

n = int(input("Nhập số lượng số nguyên n: "))
first = int(input("Nhập số thứ 1: "))
print("Ước chung lớn nhất là:", ucln_list(1, n, first))
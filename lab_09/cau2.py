def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)

def ucln_day(so_list):
    if len(so_list) == 1:
        return so_list[0]
    else:
        return ucln(so_list[0], ucln_day(so_list[1:]))

n = int(input("Nhập số lượng phần tử: "))
day_so = []
for i in range(n):
    x = int(input(f"Nhập số thứ {i+1}: "))
    day_so.append(x)

print("Ước chung lớn nhất là:", ucln_day(day_so))

def tim_ga_cho(n, c):
    for ga in range(n + 1):
        cho = n - ga
        if 2 * ga + 4 * cho == c:
            return ga, cho
    return None
n = int(input("Nhập tổng số con (gà + chó): "))
c = int(input("Nhập tổng số chân: "))
kq = tim_ga_cho(n, c)
if kq:
    ga, cho = kq
    print(f"Có {ga} con gà và {cho} con chó.")
else:
    print("Không có cách nào để chia số con gà và chó thỏa điều kiện.")

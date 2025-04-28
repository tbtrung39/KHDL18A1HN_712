def ga_cho(g, c):
    if g + c == 36 and g * 2 + c * 4 == 100:
        return g, c
    if g > 36 or c > 36:
        return None
    return ga_cho(g + 1, c - 1)

def tim_ga_cho():
    return ga_cho(0, 36)

kq = tim_ga_cho()
if kq:
    print(f"Số con gà: {kq[0]}, Số con chó: {kq[1]}")
else:
    print("Không tìm được kết quả thỏa mãn.")
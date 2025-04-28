def ga_cho(g, c):
    if g < 0 or c < 0:
        return None
    if 2*g + 4*c == 100 and g + c == 36:
        return (g, c)
    return ga_cho(g-1, c+1)

result = ga_cho(36, 0)
if result:
    print(f"Số con gà: {result[0]}, Số con chó: {result[1]}")
else:
    print("Không có nghiệm!")
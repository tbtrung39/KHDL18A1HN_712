def f(g):
    c = 36 - g
    if g < 0:
        return None
    if 2 * g + 4 * c == 100:
        return g, c
    return f(g - 1)

result = f(36)
if result:
    g, c = result
    print(f"Số gà: {g}, Số chó: {c}")
else:
    print("Không tìm được nghiệm")
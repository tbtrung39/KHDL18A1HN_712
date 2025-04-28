def find_animals_reverse(g):
    c = 36 - g
    if g < 0:
        return None
    if 2 * g + 4 * c == 100:
        return g, c
    return find_animals_reverse(g - 1)

# Bắt đầu từ số gà tối đa là 36
result = find_animals_reverse(36)
if result:
    g, c = result
    print(f"Số gà: {g}, Số chó: {c}")
else:
    print("Không tìm được nghiệm")

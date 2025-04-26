def find_chicken_dog(g, c):
    if g + c == 36 and 2 * g + 4 * c == 100:
        return g, c
    if g > 36 or c > 36:
        return None
    # Thử tăng số gà trước
    result = find_chicken_dog(g + 1, c)
    if result:
        return result
    # Nếu tăng gà không được, thử tăng chó
    return find_chicken_dog(g, c + 1)

# Chạy
result = find_chicken_dog(0, 0)
if result:
    print("Số gà:", result[0])
    print("Số chó:", result[1])
else:
    print("Không tìm được kết quả")


#Câu 12:
def solve(chickens,dogs):
    if chickens + dogs == 36 and (chickens *2 + dogs *4) == 100:
        return chickens , dogs
    if chickens >36:
        return None
    return solve(chickens+1,dogs-1)
def find_animals():
    result = solve(0,36)
    if result:
        print(f"So con ga:{result[0]},So con cho:{result[1]}")
    else:
        print("Khong tim duoc loi giai")
find_animals()
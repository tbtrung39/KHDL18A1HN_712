def tim(g = 0,c=0):
    if g+c>36:
        return None
    if g + c == 36 and 2 * g + 4 * c== 100:
        return g ,c 
    return tim(g+1,c) or tim(g,c+1)

result = tim()
if result :
    print(f"Số gà:{result[0]}, Số chó : {result[1]}")
else:
    print("Không tìm được nghiệm phù hợp.")
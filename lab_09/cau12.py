def tim_ga_cho(ga):
    cho = 36 - ga
    if ga < 0 or cho < 0:
        return  # dừng nếu vượt giới hạn
    if ga * 2 + cho * 4 == 100:
        print("Số gà:", ga)
        print("Số chó:", cho)
        return
    tim_ga_cho(ga + 1)  # thử với số gà lớn hơn

tim_ga_cho(0)

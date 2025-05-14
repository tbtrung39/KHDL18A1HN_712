from random import choice
l = [x for x in range(0, 201) if x % 5 == 0 and x % 7 == 0]
n = choice(l)
print("Số ngẫu nhiên chia hết cho cả 5 và 7 (0-200):", n)
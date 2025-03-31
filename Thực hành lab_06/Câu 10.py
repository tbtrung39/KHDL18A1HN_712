#Câu 10:
import random

numbers = [x for x in range(0, 201) if x % 5 == 0 and x % 7 == 0]

random_number = random.choice(numbers)

print("Số ngẫu nhiên chia hết cho 5 và 7 trong khoảng [0, 200]:", random_number)
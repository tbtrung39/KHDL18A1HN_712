import random

num = random.choice([x for x in range(0, 201) if x % 5 == 0 and x % 7 == 0])

print(num)
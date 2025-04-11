import random

numbers = [x for x in range(201) if x % 5 == 0 and x % 7 == 0]
result = random.choice(numbers)
print(result)
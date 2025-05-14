import random
numbers = [x for x in range(0, 201) if x % 5 == 0 and x % 7 == 0]
random_number = random.choice(numbers)
print(random_number)

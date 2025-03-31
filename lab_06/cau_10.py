import random
numbers = [num for num in range(201) if num % 5 == 0 and num % 7 == 0]
random_number = random.choice(numbers)
print("Số ngẫu nhiên chia hết cho 5 và 7 là:", random_number)

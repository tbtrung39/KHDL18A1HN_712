# Câu 10
import random
numbers = [i for i in range(201) if i % 5 == 0 and i % 7 == 0]
random_number = random.choice(numbers)
print("So ngau nhien chia het cho 5 va 7:", random_number)
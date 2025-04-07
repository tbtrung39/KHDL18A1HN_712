import random
import string

A = set(random.sample(string.ascii_letters, 5))
B = set(random.sample(string.ascii_letters, 5))

only_in_A_or_B = A.symmetric_difference(B)

print("Tập A:", A)
print("Tập B:", B)
print("Các phần tử chỉ có trong A hoặc B:", only_in_A_or_B)

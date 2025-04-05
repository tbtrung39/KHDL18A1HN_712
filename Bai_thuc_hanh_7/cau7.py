import random
import string
A= set(random.choices(string.ascii_letters + string.digits, k = 7))
B = set(random.choices(string.ascii_letters + string.digits, k = 7))
print('tap hop A la: ', A)
print('tap hop B la: ', B)
print('cac phan tu chung la: ', A&B)
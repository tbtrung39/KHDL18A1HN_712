import random
A= set(random.choices(range(2,100), k = 10))
print('Tap hop so:', A)
print("phan tu nho nhat ", min(A))
print('phn tu lon nhat ', max(A))
print('Tong cac phan tu: ', sum(A))
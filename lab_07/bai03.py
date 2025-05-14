from random import randint
A = [randint(2,100) for i in range(10)]
print('Tap hop so:', A)
print("Phan tu nho nhat ", min(A))
print('Phan tu lon nhat ', max(A))
print('Tong cac phan tu: ', sum(A))
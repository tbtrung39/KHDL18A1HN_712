n = int(input())
A = [int(input()) for i in range(n)]

B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print(B)

C = [x**2 for x in A]
print(C)

D = [x for x in A if x % 3 == 0]
print(D)

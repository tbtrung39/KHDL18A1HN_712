import random
a = [random.randint(1, 99999) for _ in range(1000)]
b = sorted(a)
c = sorted(a, reverse=True)
print(b[:5])
print(c[:5])

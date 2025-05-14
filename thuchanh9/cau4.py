import itertools

n = int(input())
arr = list(range(1, n + 1))

for perm in itertools.permutations(arr):
    print(perm)

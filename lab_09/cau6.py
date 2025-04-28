import random

def random_permutation(arr, result):
    if not arr:
        return result
    idx = random.randint(0, len(arr)-1)
    result.append(arr[idx])
    arr.pop(idx)
    return random_permutation(arr, result)

n = int(input("Nhập n: "))
arr = list(range(1, n+1))
print("Hoán vị ngẫu nhiên:", random_permutation(arr, []))
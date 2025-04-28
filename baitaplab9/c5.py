def permutation(arr):
    if len(arr) == 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        x = arr[i]
        rest = arr[:i] + arr[i+1:]
        for p in permutation(rest):
            result.append([x] + p)
    return result

n = int(input("Nhập số nguyên n: "))
A = list(range(1, n+1))
kq = permutation(A)
for p in kq:
    print(p)
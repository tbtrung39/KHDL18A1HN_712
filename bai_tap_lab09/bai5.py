def permutation(arr, k=0):
    if k == len(arr):
        print(arr)
    else:
        for i in range(k, len(arr)):
            arr[k], arr[i] = arr[i], arr[k]
            permutation(arr, k + 1)
            arr[k], arr[i] = arr[i], arr[k]

n = int(input("Nhập số n: "))
arr = list(range(1, n + 1))
permutation(arr)

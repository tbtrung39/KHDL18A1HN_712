def permutation_collect(arr, l, r, result):
    if l == r:
        result.append(arr.copy())
    else:
        for i in range(l, r+1):
            arr[l], arr[i] = arr[i], arr[l]
            permutation_collect(arr, l+1, r, result)
            arr[l], arr[i] = arr[i], arr[l]  

n = int(input("Nhập n: "))
arr = list(range(1, n+1))
result = []
permutation_collect(arr, 0, n-1, result)
print("Các hoán vị:", result)
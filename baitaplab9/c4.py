def hoan_vi(arr, k, n):
    if k == n:
        print(arr)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            hoan_vi(arr, k + 1, n)
            arr[k], arr[i] = arr[i], arr[k]

n = int(input("Nhập số nguyên n: "))
A = [i for i in range(1, n+1)]
hoan_vi(A, 0, n)
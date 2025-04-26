def permute(arr, l, r):
    if l == r:
        print(arr)
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]  # hoán đổi
            permute(arr, l + 1, r)           # đệ quy
            arr[l], arr[i] = arr[i], arr[l]  # hoán đổi lại (backtrack)

n = int(input("Nhập số tự nhiên n: "))
arr = list(range(1, n + 1))

permute(arr, 0, n - 1)

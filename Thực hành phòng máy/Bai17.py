n = int(input("Nhập bậc của ma trận đơn vị: "))
ma_tran = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print("Ma trận đơn vị:")
for hang in ma_tran:
    print(hang)

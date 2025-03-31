m, n = map(int, input("Nhập số hàng (m) và số cột (n), cách nhau bằng dấu phẩy: ").split(","))
ma_tran = []
print("Nhập các phần tử của ma trận:")
for i in range(m):
    hang = list(map(int, input(f"Nhập hàng {i + 1} (các số cách nhau bằng dấu cách): ").split()))
    ma_tran.append(hang)
tong = sum(sum(hang) for hang in ma_tran)
print("Ma trận vừa nhập:")
for hang in ma_tran:
    print(hang)
print("Tổng các phần tử của ma trận:", tong)
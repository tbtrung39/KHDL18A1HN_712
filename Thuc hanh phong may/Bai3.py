import random
def sinh_tap_hop_so_thuc():
    n = int(input("Nhập số phần tử n: "))
    A = set()
    while len(A) < n:
        A.add(round(random.uniform(0, 100), 2))
    print("Tập hợp A:", A)
    print("Phần tử nhỏ nhất:", min(A))
    print("Phần tử lớn nhất:", max(A))
    print("Tổng các phần tử:", round(sum(A), 2))
sinh_tap_hop_so_thuc()

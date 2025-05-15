from functools import reduce
n = int(input("Nhập số lượng phần tử n: "))
danh_sach = []
for i in range(n):
    while True:
        try:
            so = int(input(f"Nhập phần tử thứ {i+1}: "))
            danh_sach.append(so)
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach))
tong = reduce(lambda x, y: x + y, so_chan, 0)
print("Danh sách ban đầu:", danh_sach)
print("Các số chẵn:", so_chan)
print("Tổng các số chẵn:", tong)
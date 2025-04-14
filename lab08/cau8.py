def so_chan(lst):
    return [x for x in lst if x % 2 == 0]

lst = list(map(int, input("Nhập danh sách số nguyên: ").split()))
print("Các số chẵn:", so_chan(lst))
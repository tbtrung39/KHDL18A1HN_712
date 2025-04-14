def loc_le(lst):
    return list(filter(lambda x: x % 2 != 0, lst))

lst = [int(input("Nhập số: ")) for _ in range(int(input("Nhập số lượng phần tử: ")))]
print("Các số lẻ:", loc_le(lst))

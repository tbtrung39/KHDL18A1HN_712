def tao_list_nhap():
    n = int(input("Nhập số lượng phần tử: "))
    lst = []
    for _ in range(n):
        so = int(input("Nhập số nguyên: "))
        lst.append(so)
    return lst

def binh_phuong_so_le(lst):
    le = list(filter(lambda x: x % 2 != 0, lst))
    return list(map(lambda x: x**2, le))

lst = tao_list_nhap()
lst_le_binh_phuong = binh_phuong_so_le(lst)
print("Danh sách bình phương các số lẻ:", lst_le_binh_phuong)

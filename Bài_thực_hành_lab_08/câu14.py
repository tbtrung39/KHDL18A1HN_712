def tao_list_nhap():
    n = int(input("Nhập số lượng phần tử: "))
    lst = []
    for _ in range(n):
        so = int(input("Nhập số nguyên: "))
        lst.append(so)
    return lst

def binh_phuong_list(lst):
    return list(map(lambda x: x**2, lst))

lst = tao_list_nhap()
lst_binh_phuong = binh_phuong_list(lst)
print("Danh sách bình phương:", lst_binh_phuong)

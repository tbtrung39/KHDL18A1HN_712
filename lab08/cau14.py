def binh_phuong_list(lst):
    return list(map(lambda x: x**2, lst))

lst = [int(input("Nhập số: ")) for _ in range(int(input("Nhập số lượng phần tử: ")))]
print("Bình phương:", binh_phuong_list(lst))
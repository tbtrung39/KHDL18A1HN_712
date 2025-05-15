def bai_7():
    chuoi_A = input("Nhập chuỗi cho tập hợp A: ")
    chuoi_B = input("Nhập chuỗi cho tập hợp B: ")
    A = set(chuoi_A)
    B = set(chuoi_B)
    chi_trong_A = A - B
    chi_trong_B = B - A
    giao_AB = A & B
    print("Tập hợp A:", A)
    print("Tập hợp B:", B)
    print("Chỉ có trong A:", chi_trong_A)
    print("Chỉ có trong B:", chi_trong_B)
    print("Có trong cả A và B:", giao_AB)
bai_7()

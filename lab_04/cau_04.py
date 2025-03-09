
def nhap_phan_so():
    while True:
        tu_so = int(input("Nhập tử số của phân số: "))
        mau_so = int(input("Nhập mẫu số của phân số: "))
        if mau_so == 0:
            print("Mẫu số không được là 0. Vui lòng nhập lại!")
        else:
            return tu_so, mau_so
tu_so, mau_so = nhap_phan_so()
print(f"Phân số bạn nhập là: {tu_so}/{mau_so}")

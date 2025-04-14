def nhap_va_hien_thi(n):
    lst = [int(input(f"Nhập số nguyên thứ {i+1}: ")) for i in range(n)]
    return lst

n = int(input("Nhập số lượng phần tử: "))
lst = nhap_va_hien_thi(n)
print("Danh sách:", lst)
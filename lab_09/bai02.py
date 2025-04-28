def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)

def nhap_va_tinh_ucln(n):
    if n == 1:
        x = int(input("Nhập số: "))
        return x
    else:
        x = int(input("Nhập số: "))
        return ucln(x, nhap_va_tinh_ucln(n - 1))

def main():
    n = int(input("Nhập số lượng số nguyên n: "))
    ket_qua = nhap_va_tinh_ucln(n)
    print("Ước chung lớn nhất là:", ket_qua)

if __name__ == "__main__":
    main()

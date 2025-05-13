# Cau 5.

def NhapTN(k):
    m = int(input("Nhap so tu nhien thu " + str(k) + ": "))
    if m <= 0:
        raise ValueError
    return m
def Sinh_list(n):
    A = []
    for i in range(1, n + 1):
        while True:
            try:
                m = NhapTN(i)
                break
            except ValueError:
                print("Nhap khong chinh xac, hay nhap lai.")
        A.append(m)
    return A
List = []
n = int(input("Nhap n: "))
List = Sinh_list(n)
print("Day so tu nhien da nhap la: ", Sinh_list(n))

# Cau 9.
def dao_nguoc(n, result = 0):
    if n == 0:
        return result
    return dao_nguoc(n // 10, result * 10 + n % 10)
n = int(input("Nhap so nguyen: "))
print("So dao nguoc la: ", dao_nguoc(n))
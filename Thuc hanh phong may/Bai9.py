def dao_nguoc_so(n, rev=0):
    if n == 0:
        return rev
    return dao_nguoc_so(n // 10, rev * 10 + n % 10)
n = int(input("Nhập số nguyên dương: "))
ket_qua = dao_nguoc_so(n)
print(f"Số đảo ngược là: {ket_qua}")

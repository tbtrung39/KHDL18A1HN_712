def dao_nguoc(so, ket_qua=0):
    if so == 0:
        return ket_qua
    return dao_nguoc(so // 10, ket_qua * 10 + so % 10)

so = int(input("Nhập một số nguyên: "))
print("Số sau khi đảo ngược là:", dao_nguoc(so))

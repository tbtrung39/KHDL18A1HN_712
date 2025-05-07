def dao_so(n, so_dao=0):
    if n == 0:
        return so_dao
    else:
        so_dao = so_dao * 10 + (n % 10)
        return dao_so(n // 10, so_dao)

so = int(input("Nhập số cần đảo ngược: "))
print("Số sau khi đảo ngược là:", dao_so(so))

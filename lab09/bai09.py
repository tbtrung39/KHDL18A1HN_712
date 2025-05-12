def dao_so(n, result=0):
    if n == 0:
        return result
    return dao_so(n // 10, result * 10 + n % 10)

n = int(input("Nhập số nguyên cần đảo ngược: "))
print("Số sau khi đảo là:", dao_so(n))
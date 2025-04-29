def luy_thua(a,n):
    if n == 0 :
        return 1
    else:
        return a * luy_thua(a,n-1)
    
a = int(input("Nhập cơ số a : "))
n = int(input("Nhập số mũ n : "))

ket_qua = luy_thua(a,n)
print(f"{a}^{n} = {ket_qua}")
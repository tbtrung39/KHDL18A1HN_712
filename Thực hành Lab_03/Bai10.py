n = int(input("Nhập số nguyên dương: "))
for _ in range(1000):
    if n > 0:
        break
    n = int(input("Vui lòng nhập lại số nguyên dương: "))
so_goc = n
ket_qua = ""
for i in range(2, n + 1):
    for _ in range(n):
        if n % i == 0:
            ket_qua += str(i) + " × "
            n = n // i
        else:
            break
print(f"Phân tích thừa số nguyên tố của {so_goc}: {ket_qua[:-3]}")

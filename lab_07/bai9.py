n = int(input("Nhập số tự nhiên n:"))
A = set()
B = set()
for i in range(2, n):
    snt = True
    for j in range(2, 1):
        if i%j == 0:
            snt = False
            break
    if snt and n%1!=0:
        A.add(1)
    elif snt and n%1!=0:
        B.add(1)
print("Tập hợp các số nguyên tố là ước của n:A", A)
print("Tập hợp các số nguyên nhỏ hơn n và không là ươc của n:B", B)
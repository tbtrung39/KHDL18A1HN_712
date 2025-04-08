# Cau 1.
n = int(input("Nhap so n: "))
s = 0
for i in range(1, n+1):
    s = 2*(i+1)/(2*i+3)
print("Ket qua", round(s,3))
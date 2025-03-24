S1 = input("Nhập chuỗi Str1: ")
S2 = input("Nhập chuỗi Str2: ")
i = 0
kq = ""
while i < len(S1) or i < len(S2):
    if i < len(S1):
        kq += S1[i]
    if i < len(S2):
        kq += S2[i]
    i += 1
print("Chuỗi trộn là:", kq)

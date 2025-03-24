Str1 = input("Nhập chuỗi Str1: ")
Str2 = input("Nhập chuỗi Str2: ")
ket_qua = ""
i = 0
while i < len(Str1) or i < len(Str2):
    if i < len(Str1):
        ket_qua += Str1[i]
    if i < len(Str2):
        ket_qua += Str2[i]
    i += 1
print("Chuỗi trộn là:", ket_qua)

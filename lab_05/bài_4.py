str1 = input("Nhập chuỗi str1: ")
str2 = input("Nhập chuỗi str2: ")
ket_qua = " "
max_len = max(len(str1), len(str2))
for i in range(max_len):
    if i < len(str1):
        ket_qua+=str1[i]
    if i < len(str2):
        ket_qua+=str2[i]
print("Chuỗi sau khi trộn là : ", ket_qua)
string1 = input("Nhập chuỗi string 1: ")
string2 = input("Nhập chuỗi string 2: ")
chuoimoi = ""
i = 0
while i < len(string1) or i < len(string2):
    if i < len(string1):
        chuoimoi += string1[i]  
    if i < len(string2):
        chuoimoi += string2[i] 
    i += 1

# In kết quả
print("Chuỗi trộn là:", chuoimoi)

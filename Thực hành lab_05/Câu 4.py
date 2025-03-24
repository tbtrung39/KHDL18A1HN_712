# Câu 4:
Str1 = input("Nhập chuỗi thứ nhất: ")
Str2 = input("Nhập chuỗi thứ hai: ")
result = " "
for i in range(max(len(Str1), len(Str2))):
    if i < len(Str1):
        result += Str1[i]
    if i < len(Str2):
        result += Str2[i]
print("Chuỗi sau khi trộn:", result)
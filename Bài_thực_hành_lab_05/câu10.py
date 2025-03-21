Str1 = input("Nhập chuỗi thứ nhất: ")
Str2 = input("Nhập chuỗi thứ hai: ")
max_len = 0
chuỗi_con_max = ""
for i in range(len(Str1)):
    for j in range(len(Str2)):
        k = 0
        while i + k < len(Str1) and (j + k < len(Str2)) and (Str1[i + k] == Str2[j + k]):
            k += 1
        if k > max_len:
            max_len = k
            chuỗi_con_max = Str1[i:i + k]
print('chuỗi con dài nhât là:', chuỗi_con_max)
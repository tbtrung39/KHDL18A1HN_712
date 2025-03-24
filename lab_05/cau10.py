S1 = input("Nhập chuỗi Str1: ")
S2 = input("Nhập chuỗi Str2: ")
maxlen = 0
kq = ""
for i in range(len(S1)):
    for j in range(len(S2)):
        l = 0
        while (i + l < len(S1)) and (j + l < len(S2)) and (S1[i + l] == S2[j + l]):
            l += 1
        if l > maxlen:
            maxlen = l
            kq = S1[i:i + l]
print("Chuỗi con chung dài nhất là:", kq)

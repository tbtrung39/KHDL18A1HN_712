Str1 = input("Nhập chuỗi Str1: ")
Str2 = input("Nhập chuỗi Str2: ")
max_chung = ""
do_dai_max = 0
for i in range(len(Str1)):
    for j in range(len(Str2)):
        if Str1[i] == Str2[j]:
            do_dai = 0
            tmp = ""
            while (i + do_dai < len(Str1)) and (j + do_dai < len(Str2)) and (Str1[i + do_dai] == Str2[j + do_dai]):
                tmp += Str1[i + do_dai]
                do_dai += 1
            if do_dai > do_dai_max:
                do_dai_max = do_dai
                max_chung = tmp
print("Chuỗi con chung dài nhất là:", max_chung)

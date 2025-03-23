str1, str2 = input(), input()
lcs = ""

for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        if str1[i:j] in str2 and len(str1[i:j]) > len(lcs):
            lcs = str1[i:j]

print(lcs if lcs else "Không có chuỗi con chung.")

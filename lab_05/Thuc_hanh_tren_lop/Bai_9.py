s = input("Nhập chuỗi: ")

max = ""
ccon = s[0]

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        ccon += s[i]
    else:
        if len(ccon) > len(max):
            max = ccon
        ccpn = s[i]

if len(ccon) > len(max):
    max = ccon

print("Chuỗi con dài nhất:", max)
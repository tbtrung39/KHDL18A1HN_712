#Câu 10:
Str1 = input("Nhập chuỗi thứ nhất: ")
Str2 = input("Nhập chuỗi thứ hai: ")
max_length = 0
longest_substring = " "
for i in range(len(Str1)):
    for j in range(i, len(Str1)):
        sub =  Str1[i:j + 1]
        if sub in Str2 and len(sub) > max_length:
            max_length = len(sub)
            longest_substring = sub
print("Chuỗi con chung có độ dài cực đại :", longest_substring)
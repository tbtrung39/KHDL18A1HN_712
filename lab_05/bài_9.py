str = input("Nhập chuỗi ký tự : ")
max_char = ""
max_len = 0
i = 0
while i < len(str):
    count = 1
    while i + 1 < len(str) and str[i]== str[i +1]:
        count += 1
        i+=1
    if count > max_len:
        max_len = count
        max_char = str[i]*count
    i += 1
print("Chuỗi con có độ dài cực đại gồm ký tự giống nhau : ",max_char)
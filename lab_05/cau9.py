str = input("Nhập chuỗi ký tự: ")
max_len = 1
current_len = 1
max_char = str[0]

for i in range(1, len(str)):
    if str[i] == str[i-1]:
        current_len += 1
    else:
        current_len = 1
    if current_len > max_len:
        max_len = current_len
        max_char = str[i]

print("Chuỗi con gồm các ký tự giống nhau dài nhất là:", max_char * max_len)

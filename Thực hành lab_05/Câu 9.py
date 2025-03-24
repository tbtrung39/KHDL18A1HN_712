#Câu 9:
Str = input("Nhập chuỗi ký tự: ")
max_substring = " "
current_substring = Str[0] if Str else " "
for i in range(1, len(Str)):
    if Str[i] == Str[i - 1]:
        current_substring += Str[i]
    else:
        if len(current_substring) > len(max_substring):
            max_substring = current_substring
        current_substring = Str[i]
if len(current_substring) > len(max_substring):
    max_substring = current_substring
print("Chuỗi cọn có độ dài cực đại:", max_substring)
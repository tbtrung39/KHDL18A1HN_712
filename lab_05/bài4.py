str1 = input("Nhập chuỗi ký tự Str1: ")
str2 = input("Nhập chuỗi ký tự Str2: ")

result = ""
i, j = 0, 0
while i < len(str1) and j < len(str2):
    result += str1[i] + str2[j]
    i += 1
    j += 1

while i < len(str1):
    result += str1[i]
    i += 1

while j < len(str2):
    result += str2[j]
    j += 1

print("Chuỗi kết quả sau khi trộn:", result)
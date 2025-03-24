import re

str1 = input("Nhập chuỗi ký tự: ")

tu_list = re.split(r'[,\s]+', str1)  

print("Các từ trong chuỗi là:")
for tu in tu_list:
    if tu:  
        print(tu)

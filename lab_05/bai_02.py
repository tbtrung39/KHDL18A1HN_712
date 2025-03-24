Str = input(" nhập chuỗi ký tự :")
count = 0 
for c in Str:
    if not('a'<=c <= 'z' or 'A' <= c <= 'z'):
        count += 1
print(" Số ký tự khong phải chữ cái tiếng anh là:")        


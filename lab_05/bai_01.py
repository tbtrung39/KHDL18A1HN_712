Str = input(" nhập chuỗi ký tự: ")
count = 0
for c in str:
    if 'o' <= c <= '9':
        count += 1
print(" Số  ký tự trrong chuỗi ", count)        
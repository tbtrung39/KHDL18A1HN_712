chuoi = input("Nhập chuỗi ký tự: ")
chuoi_max = 1
do_dai = 1
max_substr = chuoi[0]  

for i in range(1, len(chuoi)):
    if chuoi[i] == chuoi[i - 1]:
        do_dai += 1  
    else:
        if do_dai > chuoi_max:
            chuoi_max = do_dai
            max_substr = chuoi[i - do_dai:i]
        do_dai = 1  

if do_dai > chuoi_max:
    chuoi_max = do_dai
    max_substr = chuoi[-do_dai:]

print(f"Chuỗi con dài nhất có các ký tự giống nhau là: '{max_substr}' với độ dài {chuoi_max}")

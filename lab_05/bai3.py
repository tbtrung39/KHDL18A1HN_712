Str = input("Nhập chuỗi nhị phân: ")
is_binary = True
for c in Str:
    if c not in '01':
        is_binary = False
        break
if is_binary:
    decimal = 0
    for i in range(len(Str)):
        decimal += int(Str[i] * (2 ** (len(Str) - 1 - i)))
    print("Số thập phân tương ứng: ", decimal)
else:
    print("Chuỗi nhập không phải nhị phân.")    

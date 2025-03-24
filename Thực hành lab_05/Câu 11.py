#Câu 11:
Str = input("Nhập chuỗi nhị phân: ")
is_binary = all(c in '01' for c in Str)
if is_binary:
    decimal = 0
    for i in range(len(Str)):
        decimal += int(Str[i]) * (2 ** (len(Str) - 1 - i))
    print("Số thập phân tương ứng: ", decimal)
else:
    print("Chuỗi nhập không phải nhị phân.")
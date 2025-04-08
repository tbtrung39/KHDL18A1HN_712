A = {123, 3.14, "hello", 7, "42", 2.71, "GPT", 100}

int_count = 0
float_count = 0
str_count = 0

for x in A:
    if type(x) == int:
        int_count += 1
    elif type(x) == float:
        float_count += 1
    elif type(x) == str:
        str_count += 1

print("Số nguyên:", int_count)
print("Số thực:", float_count)
print("Chuỗi:", str_count)

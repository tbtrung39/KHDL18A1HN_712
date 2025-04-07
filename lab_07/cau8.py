A = {1, 2.5, "hello", 3, 4.0, "world", 5}
int_count = sum(1 for x in A if isinstance(x, int))
float_count = sum(1 for x in A if isinstance(x, float))
str_count = sum(1 for x in A if isinstance(x, str))
print("Số nguyên:", int_count)
print("Số thực:", float_count)
print("Chuỗi ký tự:", str_count)
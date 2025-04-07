A = {3, 5.6, "hello", 10, "123", 7.5, "python", 2}

integers = [x for x in A if isinstance(x, int)]
floats = [x for x in A if isinstance(x, float)]
strings = [x for x in A if isinstance(x, str)]

print("Số nguyên:", len(integers))
print("Số thực:", len(floats))
print("Chuỗi:", len(strings))

import random
def sinh_tap_hop_A():
    A = set()

    while len(A) < 15:
        kieu = random.choice(['int', 'float', 'str'])
        if kieu == 'int':
            A.add(random.randint(-100, 100))
        elif kieu == 'float':
            A.add(round(random.uniform(-100, 100), 2))
        else:
            s = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
            A.add(s)
    print("Tập hợp A:", A)
    dem_int = sum(isinstance(x, int) and not isinstance(x, bool) for x in A)
    dem_float = sum(isinstance(x, float) for x in A)
    dem_str = sum(isinstance(x, str) for x in A)
    print("Số phần tử là số nguyên (int):", dem_int)
    print("Số phần tử là số thực (float):", dem_float)
    print("Số phần tử là chuỗi (str):", dem_str)
sinh_tap_hop_A()

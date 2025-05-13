def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def uoc_nguyen_to_khac_nhau(n):
    uoc_nt = set()
    for i in range(2, n + 1):
        if n % i == 0 and la_nguyen_to(i):
            uoc_nt.add(i)
    return sorted(uoc_nt)

def xu_ly_file(path_in, path_out):
    with open(path_in, 'r') as f:
        lines = f.readlines()
    
    with open(path_out, 'w') as f:
        for line in lines:
            num = int(line.strip())
            uocs = uoc_nguyen_to_khac_nhau(num)
            f.write(' '.join(map(str, uocs)) + '\n')
path_in = input("Nhập đường dẫn tới file đầu vào (VD: f_in.dat): ")
path_out = "f_out.dat"
xu_ly_file(path_in, path_out)
print(f"Đã ghi kết quả vào {path_out}")
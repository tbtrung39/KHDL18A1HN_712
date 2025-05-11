def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def uoc_nguyen_to(n):
    uoc = set()
    for i in range(2, n + 1):
        if n % i == 0 and la_nguyen_to(i):
            uoc.add(i)
    return sorted(uoc)

def xu_ly_tin(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    with open('f_out1.dat', 'w') as f:
        for line in lines:
            n = int(line.strip())
            uoc = uoc_nguyen_to(n)
            f.write(' '.join(map(str, uoc)) + '\n')
file_path=input('nhập đường dẫn đến file nội dung muốn đọc nội dung : path= ')
xu_ly_tin(file_path)

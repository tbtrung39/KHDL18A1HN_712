def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_uoc_nguyen_to(n):
    uoc_nt = []
    for i in range(2, n + 1):
        if n % i == 0 and la_nguyen_to(i):
            uoc_nt.append(i)
    return uoc_nt

with open('lab_11/f_int.dat', 'r') as f:
    lines = f.readlines()

with open('lab_11/f_out.dat', 'w') as f:
    for line in lines:
        n = int(line.strip())
        uoc = tim_uoc_nguyen_to(n)
        f.write(' '.join(map(str, uoc)) + '\n')
    f.close()
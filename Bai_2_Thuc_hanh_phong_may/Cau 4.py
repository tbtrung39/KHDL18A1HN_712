# Cau 4. Dvq
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_uoc_nguyen_to(n):
    uoc_nt = []
    for i in range(2, n + 1):
        if n % i == 0 and la_nguyen_to(i):
            uoc_nt.append(i)
    return uoc_nt

def giai_bai_tap_4(file_in = 'Bai_2_Thuc_hanh_phong_may/f_int.dat', file_out = 'Bai_2_Thuc_hanh_phong_may/f_out.dat'):
    with open(file_in , 'r') as f:
        lines = f.readlines()
    
    with open(file_out,'w') as f:
        for line in lines:
            n = int(line.strip())
            uoc = tim_uoc_nguyen_to(n)
            f.write(' '.join(map(str, uoc)) + '\n')

giai_bai_tap_4()
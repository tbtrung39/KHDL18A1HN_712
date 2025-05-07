# Cau 3. Dvq
def giai_bai_3(file_in = 'Bai_2_Thuc_hanh_phong_may/dayso1.dat', file_out = 'Bai_2_Thuc_hanh_phong_may/out1.dat'):
    with open(file_in, 'r') as f:
        line = f.readline()
        day_so = list(map(int, line.strip().split()))
    
    cac_cuc_tri = []
    for i in range(1, len(day_so) - 1):
        if (day_so[i] > day_so[i-1] and day_so[i] > day_so[i+1]) or (day_so[i] < day_so[i-1] and day_so[i] < day_so[i+1]):
            cac_cuc_tri.append(day_so[i])
    
    with open(file_out, 'w') as f:
        f.write(f"{len(cac_cuc_tri)}\n")
        f.write(' '.join(map(str,cac_cuc_tri)))

giai_bai_3()
def doc_day_so(filename):
    with open(filename, 'r') as f:
        day_so = list(map(int, f.read().split()))
    return day_so

def tim_cuc_tri(day_so):
    cuc_tri = []
    for i in range(1, len(day_so) - 1):
        if (day_so[i - 1] < day_so[i] > day_so[i + 1]) or (day_so[i - 1] > day_so[i] < day_so[i + 1]):
            cuc_tri.append(day_so[i])
    return cuc_tri

def ghi_ket_qua(filename, cuc_tri):
    with open(filename, 'w') as f:
        f.write(f"{len(cuc_tri)}\n")
        f.write(' '.join(map(str, cuc_tri)))
ds = doc_day_so(r"bai_tap\f_in.dat")
cuctri = tim_cuc_tri(ds)
ghi_ket_qua(r"bai_tap\f_in.dat", cuctri)
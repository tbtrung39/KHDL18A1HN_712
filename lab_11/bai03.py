with open('lab_11/dayso1.dat', 'r') as f:
    line = f.readline()
    day_so = list(map(int, line.strip().split()))

cac_cuc_tri = []
for i in range(1, len(day_so) - 1):
    if (day_so[i] > day_so[i-1] and day_so[i] > day_so[i+1]) or (day_so[i] < day_so[i-1] and day_so[i] < day_so[i+1]):
        cac_cuc_tri.append(day_so[i])

with open('lab_11/out1.dat', 'w') as f:
    f.write(f"{len(cac_cuc_tri)}\n")
    f.write(' '.join(map(str,cac_cuc_tri)))
    f.close()
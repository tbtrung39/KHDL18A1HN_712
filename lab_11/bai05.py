map_sbd_phach = {}
with open('lab_11/Sbd_Ph.dat', 'r') as f:
    for line in f:
        sbd, phach = map(int, line.strip().split())
        map_sbd_phach[phach] = sbd

map_sbd_ten = {}
with open('lab_11/SBD_Ten.txt', 'r') as f:
    for line in f:
        parts = line.strip().split()
        sbd = int(parts[0])
        ten = ' '.join(parts[1:])
        map_sbd_ten[sbd] = ten

thisinh_list = []
with open('lab_11/Phieu_Diem.txt', 'r') as f:
    for line in f:
        phach, diem = line.strip().split()
        phach = int(phach)
        diem = float(diem)
        sbd = map_sbd_phach.get(phach)
        hoten = map_sbd_ten.get(sbd, "Unknown")
        thisinh_list.append((sbd, hoten, diem))

thisinh_list.sort(key=lambda x: x[2], reverse=True)

with open('lab_11/Ketqua.txt', 'w') as f:
    for sbd, hoten, diem in thisinh_list:
        f.write(f"{sbd} {hoten} {diem:.2f}\n")
    f.close()

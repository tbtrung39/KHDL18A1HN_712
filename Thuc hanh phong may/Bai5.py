
def ghep_thong_tin():
    sbd_phach = {}
    with open("Sbd_Ph.dat", "r") as f:
        for line in f:
            sbd, phach = map(int, line.strip().split())
            sbd_phach[phach] = sbd
    sbd_ten = {}
    with open("Sbd_Ten.txt", "r") as f:
        for line in f:
            parts = line.strip().split()
            sbd = int(parts[0])
            ten = " ".join(parts[1:])
            sbd_ten[sbd] = ten
    ds_thi_sinh = []
    with open("Phieu_Diem.txt", "r") as f:
        for line in f:
            phach, diem = map(int, line.strip().split())
            if phach in sbd_phach:
                sbd = sbd_phach[phach]
                ten = sbd_ten.get(sbd, "???")
                ds_thi_sinh.append((sbd, ten, diem))
    ds_thi_sinh.sort(key=lambda x: -x[2])
    with open("Ketqua.txt", "w") as f:
        for sbd, ten, diem in ds_thi_sinh:
            f.write(f"{sbd} {ten} {diem}\n")
ghep_thong_tin()
with open("Ketqua.txt", "r") as f:
    print("Nội dung file Ketqua.txt:")
    print(f.read())

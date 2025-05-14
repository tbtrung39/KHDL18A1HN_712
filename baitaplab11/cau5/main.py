# Đọc SBD → Số phách
sbd_to_phach = {}
with open("Sbd_Ph.dat", "r") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 2:
            sbd, phach = parts
            sbd_to_phach[sbd] = phach

# Đọc SBD → Họ tên
sbd_to_ten = {}
with open("SBD_Ten.txt", "r") as f:
    for line in f:
        parts = line.strip().split(maxsplit=1)
        if len(parts) == 2:
            sbd, hoten = parts
            sbd_to_ten[sbd] = hoten

# Đọc số phách → Điểm
phach_to_diem = {}
with open("Phieu_Diem.txt", "r") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 2:
            phach, diem = parts
            phach_to_diem[phach] = diem

# Ghi file Ketqua.txt
with open("Ketqua.txt", "w") as f:
    for sbd in sbd_to_phach:
        phach = sbd_to_phach.get(sbd, "")
        hoten = sbd_to_ten.get(sbd, "")
        diem = phach_to_diem.get(phach, "")
        f.write(f"{sbd} {hoten} {diem}\n")
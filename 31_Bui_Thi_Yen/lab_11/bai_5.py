def ghep_phach():
    sbd_to_phach = {}
    with open("Sbd_Ph.dat", "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                sbd, phach = parts
                sbd_to_phach[int(sbd)] = int(phach)

    sbd_to_ten = {}
    with open("SBD_Ten.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(maxsplit=1)
            if len(parts) == 2:
                sbd, hoten = parts
                sbd_to_ten[int(sbd)] = hoten

    phach_to_diem = {}
    with open("Phieu_Diem.txt", "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                phach, diem = parts
                phach_to_diem[int(phach)] = float(diem)

    ketqua = []
    for sbd in sbd_to_phach:
        phach = sbd_to_phach[sbd]
        hoten = sbd_to_ten.get(sbd, "Khong ro")
        diem = phach_to_diem.get(phach, 0.0)
        ketqua.append((sbd, hoten, diem))
    ketqua.sort(key=lambda x: x[2], reverse=True)
    with open("Ketqua.txt", "w", encoding="utf-8") as f:
        for sbd, hoten, diem in ketqua:
            f.write(f"{sbd} {hoten} {diem}\n")

    print("Đã ghép phách và ghi vào file Ketqua.txt.")
ghep_phach()
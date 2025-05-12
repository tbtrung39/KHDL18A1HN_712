def ghep_file():
    with open(r"bai_tap\Sbd_Ph.dat", 'r') as f1, open(r"bai_tap\Sbd_Ten.txt", 'r') as f2, open(r"bai_tap\Phieu_Diem.txt", 'r') as f3:
        sbd = f1.readlines()
        ten = f2.readlines()
        diem = f3.readlines()
    with open('ghepdiem.txt', 'w') as f:
        for i in range(len(sbd)):
            f.write(f"{sbd[i].strip()} {ten[i].strip()} {diem[i].strip()}\n")

ghep_file()

with open('Sbd_Ph.dat', 'w') as f:
    f.write('101 201\n')
    f.write('102 202\n')
    f.write('103 203\n')

with open('Sbd_Ten.txt', 'w') as f:
    f.write('101 Nguyen Van A\n')
    f.write('102 Tran Thi B\n')
    f.write('103 Le Van C\n')

with open('Phieu_Diem.txt', 'w') as f:
    f.write('201 8.5\n')
    f.write('202 9.0\n')
    f.write('203 7.5\n')

sbd_ph = {}
with open('Sbd_Ph.dat', 'r') as f:
    for line in f:
        sbd, phach = line.strip().split()
        sbd_ph[sbd] = phach

sbd_ten = {}
with open('Sbd_Ten.txt', 'r') as f:
    for line in f:
        parts = line.strip().split()
        sbd = parts[0]
        ten = ' '.join(parts[1:])
        sbd_ten[sbd] = ten
phach_diem = {}
with open('Phieu_Diem.txt', 'r') as f:
    for line in f:
        phach, diem = line.strip().split()
        phach_diem[phach] = float(diem)


ds_sinhvien = []

for sbd in sbd_ph:
    phach = sbd_ph[sbd]
    diem = phach_diem.get(phach, 0)
    ten = sbd_ten.get(sbd, "Unknown")
    ds_sinhvien.append((sbd, ten, diem))

ds_sinhvien.sort(key=lambda x: x[2], reverse=True)

with open('Ketqua.txt', 'w') as f:
    for sv in ds_sinhvien:
        f.write(f"{sv[0]} {sv[1]} {sv[2]}\n")

print("Đã ghi kết quả vào file Ketqua.txt!")
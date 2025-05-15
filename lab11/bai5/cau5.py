def read_sbd_phach(filename1):
    sbd_to_phach = {}
    with open(filename1, 'r') as f:
        for line in f:
            sbd, phach = map(int, line.strip().split())
            sbd_to_phach[sbd] = phach
    return sbd_to_phach

def read_sbd_ten(filename2):
    sbd_to_ten = {}
    with open(filename2, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            sbd = int(parts[0])
            ten = ' '.join(parts[1:])
            sbd_to_ten[sbd] = ten
    return sbd_to_ten

def read_phach_diem(filename3):
    phach_to_diem = {}
    with open(filename3, 'r') as f:
        for line in f:
            phach, diem = map(float, line.strip().split())
            phach_to_diem[phach] = diem
    return phach_to_diem

filename1=read_sbd_phach(input('nhập đường dẫn đến file nội dung muốn đọc nội dung gồm Sbd và số phách :  '))
filename2=read_sbd_ten(input('nhập đường dẫn đến file nội dung muốn đọc nội dung gồm Sbd và tên :  '))
filename3=read_phach_diem(input('nhập đường dẫn đến file nội dung muốn đọc nội dung gồm số phách và điểm : '))

thi_sinh = []
for sbd, phach in filename1.items():
    if sbd in filename2 and phach in filename3:
        thi_sinh.append({
            'sbd': sbd,
            'ten': filename2[sbd],
            'diem': filename3[phach]
        })

thi_sinh_sorted = sorted(thi_sinh, key=lambda x: x['diem'], reverse=True)

with open('Ketqua.txt', 'w', encoding='utf-8') as f:
    for ts in thi_sinh_sorted:
        f.write(f"{ts['sbd']} {ts['ten']} {ts['diem']}\n")

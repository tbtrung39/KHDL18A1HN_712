def doc_file_tap_tin(ten_file):
    with open(ten_file, 'r') as f:
        dong = f.readlines()

    so_dong = int(dong[0].strip())
    ma_tran = [list(map(int, dong[i].strip().split())) for i in range(1, len(dong))]
    return so_dong, ma_tran, dong

def hien_thi_dong_dau_va_thu_ba(dong):
    print("Dòng đầu tiên:", dong[0].strip())
    if len(dong) >= 3:
        print("Dòng thứ ba:", dong[2].strip())
    else:
        print("Không có dòng thứ ba trong file.")

def hien_thi_toan_bo_file(dong):
    print("\nToàn bộ nội dung file:")
    for d in dong:
        print(d.strip())

def ghi_ma_tran_le(ma_tran, ten_file_moi):
    with open(ten_file_moi, 'w') as f:
        for hang in ma_tran:
            hang_moi = [str(x) if x % 2 != 0 else '0' for x in hang]
            f.write(' '.join(hang_moi) + '\n')

def in_dong_cuoi_file(ten_file):
    with open(ten_file, 'r') as f:
        cac_dong = f.readlines()
        if cac_dong:
            print("\nDòng cuối trong ODD.txt:", cac_dong[-1].strip())

ten_file_dau_vao = 'matrix.txt'
ten_file_odd = 'ODD.txt'

so_dong, ma_tran, cac_dong = doc_file_tap_tin(ten_file_dau_vao)
hien_thi_dong_dau_va_thu_ba(cac_dong)
hien_thi_toan_bo_file(cac_dong)
ghi_ma_tran_le(ma_tran, ten_file_odd)
in_dong_cuoi_file(ten_file_odd)

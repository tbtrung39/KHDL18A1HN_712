# Cau 1. Dvq
def giai_bai_1(ten_tep_dau_vao="Bai_2_Thuc_hanh_phong_may/dayso.dat"):
    with open(ten_tep_dau_vao,'r') as f:
        for line in f:
            cac_so_str=line.strip().split()
            cac_so=[int(so) for so in cac_so_str]
            tong=sum(cac_so)
    print(f"Dong: {line.strip()},tong: {tong}")
giai_bai_1()
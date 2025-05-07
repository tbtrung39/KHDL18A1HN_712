# Cau 7. Dvq
def giai_bai_tap_7(file_m='Bai_2_Thuc_hanh_phong_may/m_nums.txt', file_n='Bai_2_Thuc_hanh_phong_may/n_num.txt', file_out='Bai_2_Thuc_hanh_phong_may/so_chung.txt'):
    with open(file_m, 'r') as f:
        m_data = list(map(int, f.read().split()))

    with open(file_n, 'r') as f:
        n_data = list(map(int, f.read().split()))

    so_chung = sorted(set(m_data) & set(n_data))

    with open(file_out, 'w') as f:
        f.write(' '.join(map(str, so_chung)))

    print("Cac so chung cua hai file la: ")
    print(' '.join(map(str, so_chung)))

giai_bai_tap_7()
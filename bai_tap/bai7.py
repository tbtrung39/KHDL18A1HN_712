def tim_so_chung(file1, file2, file_out):
    with open(file1, 'r') as f1:
        data1 = set(map(int, f1.read().split()))
    with open(file2, 'r') as f2:
        data2 = set(map(int, f2.read().split()))
    chung = sorted(data1 & data2)
    with open(file_out, 'w') as f_out:
        f_out.write(' '.join(map(str, chung)))
tim_so_chung(r"bai_tap\m_num.txt",r"bai_tap\n_num.txt", 'common.txt')
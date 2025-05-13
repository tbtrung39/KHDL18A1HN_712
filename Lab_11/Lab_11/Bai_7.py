def doc_so_tu_file():
    with open('n_nums.txt', 'r') as f1:
        noi_dung_1 = f1.read()

    with open('m_nums.txt', 'r') as f2:
        noi_dung_2 = f2.read()

    n_list = list(map(int, noi_dung_1.strip().split()))
    m_list = list(map(int, noi_dung_2.strip().split()))
    return n_list, m_list

def tim_so_chung(n_list, m_list):
    return list(set(n_list) & set(m_list))

def ghi_file_so_chung(so_chung):
    with open('so_chung.txt', 'w') as f:
        f.write(' '.join(map(str, so_chung)))

def main():
    n_list, m_list = doc_so_tu_file()
    so_chung = tim_so_chung(n_list, m_list)
    ghi_file_so_chung(so_chung)
    print("Các số chung là:")
    print(' '.join(map(str, so_chung)))

main()

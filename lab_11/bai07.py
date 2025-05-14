with open('lab_11/m_nums.txt', 'r') as f:
    m_data = list(map(int, f.read().split()))

with open('lab_11/n_num.txt', 'r') as f:
    n_data = list(map(int, f.read().split()))

so_chung = sorted(set(m_data) & set(n_data))

with open('lab_11/n_num.txt', 'w') as f:
    f.write(' '.join(map(str, so_chung)))
    f.close()

print("Cac so chung cua hai file la: ")
print(' '.join(map(str, so_chung)))
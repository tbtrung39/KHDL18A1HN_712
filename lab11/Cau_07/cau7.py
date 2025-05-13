
fileM = input('Nhập đường dẫn đến file m_num.txt: ')
fileN = input('Nhập đường dẫn đến file n_num.txt: ')

with open(fileM, 'r') as f:
    m_numbers = set(map(int, f.read().split()))

with open(fileN, 'r') as f:
    n_numbers = set(map(int, f.read().split()))

common_numbers = sorted(m_numbers & n_numbers)

with open('so_chung.txt', 'w') as f:
    for num in common_numbers:
        f.write(f"{num}\n")

print("Các số chung trong cả hai file:")
with open('so_chung.txt', 'r') as f:
    print(f.read())
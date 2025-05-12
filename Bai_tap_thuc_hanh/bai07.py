file1 = input('Nhập đường dẫn đến file1: ')
file2 = input('Nhập đường dẫn đến file2: ')

with open(file1, 'r') as f:
    m_numbers = set(map(int, f.read().split()))

with open(file2, 'r') as f:
    n_numbers = set(map(int, f.read().split()))

so_chung = sorted(m_numbers & n_numbers)

with open('so_chung.txt', 'w') as f:
    for num in so_chung:
        f.write(f"{num}\n")

print("Các số chung trong cả hai file:")
with open('so_chung.txt', 'r') as f:
    print(f.read())
# Tạo dữ liệu mẫu cho m_nums.txt và n_nums.txt
with open('m_nums.txt', 'w') as f:
    f.write('1 2 3 4 5 6 7 8 9 10')

with open('n_nums.txt', 'w') as f:
    f.write('5 6 7 12 13 14 1 20')
def read_numbers_from_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
        return list(map(int, content.split()))
m_nums = read_numbers_from_file('m_nums.txt')
n_nums = read_numbers_from_file('n_nums.txt')
common_nums = list(set(m_nums) & set(n_nums))
with open('so_chung.txt', 'w') as f:
    f.write(' '.join(map(str, sorted(common_nums))))
with open('so_chung.txt', 'r') as f:
    print("Các số chung là:")
    print(f.read())

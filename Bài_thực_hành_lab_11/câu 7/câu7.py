fileM = input('Nhập đường dẫn đến file m_num.txt: ')
fileN = input('Nhập đường dẫn đến file n_num.txt: ')

# Đọc dữ liệu từ file m_num.txt
with open(fileM, 'r') as f:
    m_numbers = set(map(int, f.read().split()))

# Đọc dữ liệu từ file n_num.txt
with open(fileN, 'r') as f:
    n_numbers = set(map(int, f.read().split()))

# Tìm các số chung
common_numbers = sorted(m_numbers & n_numbers)

# Ghi kết quả vào file so_chung.txt
with open('so_chung.txt', 'w') as f:
    for num in common_numbers:
        f.write(f"{num}\n")

# In nội dung file so_chung.txt ra màn hình
print("Các số chung trong cả hai file:")
with open('so_chung.txt', 'r') as f:
    print(f.read())

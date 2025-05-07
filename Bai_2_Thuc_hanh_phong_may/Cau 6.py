# Cau 6. Dvq
def tao_file_bangso(filename='Bai_2_Thuc_hanh_phong_may/bangso.txt'):
    noi_dung = """4
211 133 180 5
192 168 1 254
11 1 11 233
"""
    with open(filename, 'w') as f:
        f.write(noi_dung)

def giai_bai_tap_6(file_in='Bai_2_Thuc_hanh_phong_may/bangso.txt', file_odd='Bai_2_Thuc_hanh_phong_may/ODD.txt'):
    with open(file_in, 'r') as f:
        lines = f.readlines()

# a. 
    print("Dong dau tientien:", lines[1].strip())
    print("Dong thu 33:", lines[3].strip())

# b. 
    print("\nNoi dung toan bo file:")
    for line in lines:
        print(line.strip())

# c.
    matrix = []
    for line in lines[1:]:  
        nums = list(map(int, line.strip().split()))
        row = [num if num % 2 == 1 else 0 for num in nums]
        matrix.append(row)

    with open(file_odd, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')

# d.
    with open(file_odd, 'r') as f:
        last_line = f.readlines()[-1]
        print("\nDong cuoicuoi ODD.txt:", last_line.strip())

tao_file_bangso()
giai_bai_tap_6()
with open("m_nums.txt", "w") as f:
    f.write("1 3 5 7 9 11 13")
with open("n_num.txt", "w") as f:
    f.write("2 3 6 9 12 15")

def doc_file_so_nguyen(ten_file):
    with open(ten_file, "r") as f:
        return set(map(int, f.read().split()))

tap_m = doc_file_so_nguyen("m_nums.txt")
tap_n = doc_file_so_nguyen("n_num.txt")
so_chung = sorted(tap_m & tap_n)

with open("so_chung.txt", "w") as f:
    f.write(" ".join(map(str, so_chung)))

print("Các số xuất hiện ở cả hai file là:")
print(" ".join(map(str, so_chung)))
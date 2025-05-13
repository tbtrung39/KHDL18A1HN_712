def uoc_so_tu_nhien(n):
    uoc = []
    for i in range(1, n + 1):
        if n % i == 0:
            uoc.append(i)
    return uoc

def xu_ly_file_uoc_so():
    with open("in.dat", "r") as f:
        numbers = [int(line.strip()) for line in f if line.strip()]

    with open("f_out.dat", "w") as f:
        for num in numbers:
            uoc = uoc_so_tu_nhien(num)
            f.write(" ".join(map(str, uoc)) + "\n")

    print("Đã ghi các ước vào f_out.dat.")

with open("f_in.dat", "w") as f:
    f.write("6\n12\n9\n")

xu_ly_file_uoc_so()

with open("f_in.dat", "w") as f:
    f.write("12\n18\n28\n30")
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def uoc_nguyen_to(n):
    uoc = []
    for i in range(2, n + 1):
        if n % i == 0 and la_nguyen_to(i):
            uoc.append(i)
    return uoc
def xu_ly_uoc_so_nguyen_to(tep_vao, tep_ra):
    with open(tep_vao, "r") as f:
        cac_so = [int(line.strip()) for line in f]

    with open(tep_ra, "w") as f:
        for so in cac_so:
            uoc = uoc_nguyen_to(so)
            f.write(" ".join(map(str, uoc)) + "\n")

xu_ly_uoc_so_nguyen_to("f_in.dat", "f_out.dat")
with open("f_out.dat", "r") as f:
    print("Nội dung f_out.dat:")
    print(f.read())

with open("f_in.dat", "w") as f:
    f.write("1 3 2 4 5 3 6 1 7")
def la_cuc_tri(a_truoc, a_hien_tai, a_sau):
    return (a_truoc < a_hien_tai > a_sau) or (a_truoc > a_hien_tai < a_sau)
def tim_cac_phan_tu_cuc_tri(tep_vao, tep_ra):
    with open(tep_vao, "r") as f:
        day_so = list(map(int, f.read().strip().split()))
    cac_cuc_tri = []
    for i in range(1, len(day_so) - 1):
        if la_cuc_tri(day_so[i - 1], day_so[i], day_so[i + 1]):
            cac_cuc_tri.append(day_so[i])
    with open(tep_ra, "w") as f:
        f.write(f"{len(cac_cuc_tri)}\n")
        f.write(" ".join(map(str, cac_cuc_tri)))
tim_cac_phan_tu_cuc_tri("f_in.dat", "f_out.dat")
with open("f_out.dat", "r") as f:
    print("Nội dung tệp f_out.dat:")
    print(f.read())

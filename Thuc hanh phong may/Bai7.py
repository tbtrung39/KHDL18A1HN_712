def tim_phan_tich(n, tong_con_lai=None, nghiem_hien_tai=None):
    if tong_con_lai is None:
        tong_con_lai = n
    if nghiem_hien_tai is None:
        nghiem_hien_tai = []
    if tong_con_lai == 0:
        print(nghiem_hien_tai)
        return
    for i in range(1, tong_con_lai + 1):
        tim_phan_tich(n, tong_con_lai - i, nghiem_hien_tai + [i])
n = int(input("Nhập số nguyên dương n: "))
print(f"Các bộ nghiệm x₁ + x₂ + ... + xₖ = {n}:")
tim_phan_tich(n)
def tim_phan_tich(n, tong_con_lai=None, nghiem_hien_tai=None):
    if tong_con_lai is None:
        tong_con_lai = n
    if nghiem_hien_tai is None:
        nghiem_hien_tai = []
    if tong_con_lai == 0:
        print(nghiem_hien_tai)
        return
    for i in range(1, tong_con_lai + 1):
        tim_phan_tich(n, tong_con_lai - i, nghiem_hien_tai + [i])
n = int(input("Nhập số nguyên dương n: "))
print(f"Các bộ nghiệm x₁ + x₂ + ... + xₖ = {n}:")
tim_phan_tich(n)

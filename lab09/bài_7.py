def tim_cac_bo_nghiem(n,so_phan_tu,bo_nghiem_hien_tai,tat_ca_bo_nghiem):
    if so_phan_tu == 1:
        bo_nghiem_hien_tai.append(n)
        tat_ca_bo_nghiem.append(bo_nghiem_hien_tai.copy())
        bo_nghiem_hien_tai.pop()
    else:
        for i in range(n +1):
            bo_nghiem_hien_tai.append(i)
            tim_cac_bo_nghiem(n -i,so_phan_tu - 1,bo_nghiem_hien_tai,tat_ca_bo_nghiem)
            bo_nghiem_hien_tai.pop()

N = int(input("Nhập số tự nhiên N : "))
so_phan_tu = int(input("Nhập số lượng phần tử cần phân tích : "))
tat_cac_bo_nghiem = []
tim_cac_bo_nghiem(N,so_phan_tu,[],tat_cac_bo_nghiem)
print(f'Tất cả các bộ nghiệm của {N} với {so_phan_tu} phần tử : ')
for bo_nghiem in tat_cac_bo_nghiem:
    print(bo_nghiem)
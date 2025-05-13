def doc_file_vao():
    with open("PASSENGER.IN", "r") as f:
        dong = f.readlines()

    so_khach = int(dong[0])
    du_lieu_hanh_ly = []

    for dong_hanh_ly in dong[2:]:
        hanh_ly = list(map(float, dong_hanh_ly.strip().split()))
        du_lieu_hanh_ly.append(hanh_ly)

    return du_lieu_hanh_ly


def tinh_tong_trong_luong(hanh_ly_cua_khach):
    return [sum(hanh_ly) for hanh_ly in hanh_ly_cua_khach]


def kiem_tra_bi_huy(hanh_ly_cua_khach):
    danh_sach_bi_huy = []
    for thu_tu, hanh_ly in enumerate(hanh_ly_cua_khach, start=1):
        if sum(hanh_ly) > 23 or len(hanh_ly) > 5:
            danh_sach_bi_huy.append(thu_tu)
    return danh_sach_bi_huy


def ghi_file_trong_luong(danh_sach):
    with open("WEIGHT.OUT", "w") as f:
        for so in danh_sach:
            f.write(f"{so:.2f}\n")


def ghi_file_huy(danh_sach):
    with open("CANCELED.OUT", "w") as f:
        for so in danh_sach:
            f.write(f"{so}\n")


def main():
    hanh_ly = doc_file_vao()

    danh_sach_trong_luong = tinh_tong_trong_luong(hanh_ly)
    danh_sach_bi_huy = kiem_tra_bi_huy(hanh_ly)

    ghi_file_trong_luong(danh_sach_trong_luong)
    ghi_file_huy(danh_sach_bi_huy)

    print("Các hành khách bị huỷ chuyến là:")
    for stt in danh_sach_bi_huy:
        print(f"- Hành khách thứ {stt}")

main()

import math
def chuyen_doi_thoi_gian(s):
    d = s // (24 * 3600)
    s %= 24 * 3600
    h = s // 3600
    s %= 3600
    m = s // 60
    s %= 60
    return f"{d} ngày, {h} giờ, {m} phút, {s} giây"
tong_so_giay = int(input("Nhập tổng số giây: "))
ket_qua = chuyen_doi_thoi_gian(tong_so_giay)
print("Kết quả:", ket_qua)
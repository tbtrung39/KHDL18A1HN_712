def ngay_tiep_theo(ngay, thang):
    so_ngay_trong_thang = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if not (1 <= thang <= 12 and 1 <= ngay <= so_ngay_trong_thang[thang]):
        return "Ngày tháng không hợp lệ"

    ngay += 1
    if ngay > so_ngay_trong_thang[thang]:
        ngay = 1
        thang += 1
        if thang > 12:
            thang = 1

    return f"{ngay}/{thang}"

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
print(f"Ngày tiếp theo là: {ngay_tiep_theo(ngay, thang)}")
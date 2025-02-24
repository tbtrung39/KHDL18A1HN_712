def tinh_tien_dien(kw):
    if 0 <= kw <= 100:
        return kw * 2000
    elif 101 <= kw <= 200:
        return 100 * 2000 + (kw - 100) * 2500
    elif 201 <= kw <= 300:
        return 100 * 2000 + 100 * 2500 + (kw - 200) * 3000
    else:
        return 100 * 2000 + 100 * 2500 + 100 * 3000 + (kw - 300) * 5000

so_kw = int(input("Nhập số KW điện tiêu thụ: "))
print(f"Tiền điện phải trả: {tinh_tien_dien(so_kw):,.0f} đồng")

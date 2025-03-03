def ngay_tiep_theo(ngay, thang):
    """
    Tìm ngày tiếp theo của một ngày cho trước trong năm không nhuận.

    Args:
        ngay (int): Ngày hiện tại.
        thang (int): Tháng hiện tại.

    Returns:
        tuple: Ngày và tháng của ngày tiếp theo, hoặc thông báo lỗi.
    """

    # Kiểm tra tính hợp lệ của ngày và tháng
    if not (1 <= thang <= 12 and 1 <= ngay <= 31):
        return "Ngày hoặc tháng không hợp lệ"

    # Số ngày trong mỗi tháng
    so_ngay_trong_thang = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    # Tính ngày tiếp theo
    if ngay < so_ngay_trong_thang[thang]:
        ngay += 1
    else:
        ngay = 1
        if thang == 12:
            thang = 1
        else:
            thang += 1

    return ngay, thang

# Ví dụ sử dụng
ngay_hien_tai = 31
thang_hien_tai = 12
ngay_tiep, thang_tiep = ngay_tiep_theo(ngay_hien_tai, thang_hien_tai)

if isinstance(ngay_tiep, str):
    print(ngay_tiep)  # In ra thông báo lỗi nếu có
else:
    print(f"Ngày tiếp theo là: {ngay_tiep}/{thang_tiep}")
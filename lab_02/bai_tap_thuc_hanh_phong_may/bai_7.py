def xep_loai_hoc_luc(diem):
    if 0.0 <= diem <= 3.0:
        return "Loại Kém"
    elif diem == 4.0:
        return "Loại Yếu"
    elif 5.0 <= diem <= 6.0:
        return "Loại Trung bình"
    elif 7.0 <= diem <= 8.0:
        return "Loại Khá"
    elif 9.0 <= diem <= 10.0:
        return "Loại Giỏi"
    else:
        return "Điểm không hợp lệ"

diem = float(input("Nhập điểm trung bình: "))
print(xep_loai_hoc_luc(diem))
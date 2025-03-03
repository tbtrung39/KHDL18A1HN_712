def xep_loai_hoc_luc(diem):
    if 0 <= diem <= 3:
        return "Loại Kém"
    elif diem == 4:
        return "Loại Yếu"
    elif 5 <= diem <= 6:
        return "Loại Trung bình"
    elif 7 <= diem <= 8:
        return "Loại Khá"
    elif 9 <= diem <= 10:
        return "Loại Giỏi"
    else:
        return "Điểm không hợp lệ"
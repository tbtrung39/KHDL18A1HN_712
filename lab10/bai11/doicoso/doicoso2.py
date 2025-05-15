
def loc_chuoi_16(chuoi):
    """Loại bỏ các ký tự không thuộc {0-9, A-F}"""
    tap_hop_hop_le = set('0123456789ABCDEF')
    ket_qua = ''.join(c for c in chuoi.upper() if c in tap_hop_hop_le)
    print(f"Chuỗi hợp lệ sau khi loại bỏ ký tự sai: {ket_qua}")
    return ket_qua

def xac_dinh_co_so(chuoi):
    """Xác định chuỗi thuộc cơ số nào"""
    chuoi = chuoi.upper()
    if all(c in '01' for c in chuoi):
        return 2
    elif all(c in '01234567' for c in chuoi):
        return 8
    elif all(c in '0123456789' for c in chuoi):
        return 10
    elif all(c in '0123456789ABCDEF' for c in chuoi):
        return 16
    else:
        return None  # Không xác định được

def doi_co_so_2_sang_10(chuoi):
    """Chuyển chuỗi từ cơ số 2 sang cơ số 10"""
    try:
        so = int(chuoi, 2)
        print(f"Số {chuoi} ở cơ số 2 = {so} ở cơ số 10")
        return so
    except ValueError:
        print("Chuỗi không hợp lệ cho cơ số 2.")
        return None

def doi_co_so_8_sang_10(chuoi):
    """Chuyển chuỗi từ cơ số 8 sang cơ số 10"""
    try:
        so = int(chuoi, 8)
        print(f"Số {chuoi} ở cơ số 8 = {so} ở cơ số 10")
        return so
    except ValueError:
        print("Chuỗi không hợp lệ cho cơ số 8.")
        return None

def doi_co_so_16_sang_10(chuoi):
    """Chuyển chuỗi từ cơ số 16 sang cơ số 10"""
    try:
        so = int(chuoi, 16)
        print(f"Số {chuoi} ở cơ số 16 = {so} ở cơ số 10")
        return so
    except ValueError:
        print("Chuỗi không hợp lệ cho cơ số 16.")
        return None
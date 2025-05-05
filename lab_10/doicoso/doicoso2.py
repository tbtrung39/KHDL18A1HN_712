def bieu_dien_he_co_so(s):
    try:
        return int(s, 2), int(s, 8), int(s, 16)
    except ValueError:
        return "Không hợp lệ"

def doi_2_sang_10(s):
    return int(s, 2)

def doi_8_sang_10(s):
    return int(s, 8)

def doi_16_sang_10(s):
    return int(s, 16)
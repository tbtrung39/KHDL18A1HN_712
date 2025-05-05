def loai_bo_ky_tu_khong_hop_le(s):
    hop_le = '0123456789ABCDEF'
    ket_qua = ''.join([c for c in s.upper() if c in hop_le])
    return ket_qua

def xac_dinh_co_so(s):
    s = s.upper()
    if all(c in '01' for c in s):
        return 2
    elif all(c in '01234567' for c in s):
        return 8
    elif all(c in '0123456789' for c in s):
        return 10
    elif all(c in '0123456789ABCDEF' for c in s):
        return 16
    else:
        return -1

def doi_co_so_2_sang_10(s):
    return int(s, 2)

def doi_co_so_8_sang_10(s):
    return int(s, 8)

def doi_co_so_16_sang_10(s):
    return int(s, 16)

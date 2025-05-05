# Xoa cac ky tu khong hop le khoi chuoi
def xoa_ky_tu_khong_hop_le(s):
    ky_tu_hop_le = "0123456789ABCDEF"
    return ''.join([c for c in s.upper() if c in ky_tu_hop_le])

# Xac dinh he co so cua chuoi
def xac_dinh_he_co_so(s):
    s = xoa_ky_tu_khong_hop_le(s)
    ky_tu_lon_nhat = max(s)
    if ky_tu_lon_nhat.isdigit():
        return int(ky_tu_lon_nhat) + 1
    else:
        return ord(ky_tu_lon_nhat) - ord('A') + 11

# Chuyen doi tu co so 2 sang co so 10
def co_so_2_sang_10(s):
    return int(s, 2)

# Chuyen doi tu co so 8 sang co so 10
def co_so_8_sang_10(s):
    return int(s, 8)

# Chuyen doi tu co so 16 sang co so 10
def co_so_16_sang_10(s):
    return int(s, 16)

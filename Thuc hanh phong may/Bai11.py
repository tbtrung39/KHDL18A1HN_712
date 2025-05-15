from doicoso import *

# Dùng hàm của doicoso
def doi_sang_nhi_phan(n):
    return bin(n)[2:]

def doi_sang_bat_phan(n):
    return oct(n)[2:]

def doi_sang_thap_luc_phan(n):
    return hex(n)[2:].upper()


# Dùng hàm của doicoso2

def loc_ky_tu_hop_le(chuoi):
    hop_le = '0123456789ABCDEF'
    chuoi = chuoi.upper()
    return ''.join([c for c in chuoi if c in hop_le])

def cac_co_so_hop_le(chuoi):
    hop_le_coso = []
    for base in range(2, 17):
        try:
            int(chuoi, base)
            hop_le_coso.append(base)
        except ValueError:
            continue
    return hop_le_coso

def doi_coso_ve_10(chuoi, base):
    try:
        return int(chuoi, base)
    except ValueError:
        return None


# Module: doicoso2.py

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

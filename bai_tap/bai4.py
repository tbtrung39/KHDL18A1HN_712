def giai_pt_bac_nhat(a, b):
    if a == 0:
        return "Vô nghiệm" if b != 0 else "Vô số nghiệm"
    return -b / a

def giai_pt_bac_hai(a, b, c):
    delta = b**2 - 4*a*c
    if a == 0:
        return giai_pt_bac_nhat(b, c)
    if delta < 0:
        return "Vô nghiệm"
    elif delta == 0:
        return -b / (2*a)
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return x1, x2

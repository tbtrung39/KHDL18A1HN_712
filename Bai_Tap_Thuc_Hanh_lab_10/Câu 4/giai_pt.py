import math

def giai_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình có vô số nghiệm."
        else:
            return "Phương trình vô nghiệm."
    else:
        x = -b / a
        return f"Phương trình có nghiệm duy nhất: x = {x}"

def giai_bac_hai(a, b, c):
    if a == 0:
        # Nếu a = 0 thì thành phương trình bậc nhất
        return giai_bac_nhat(b, c)
    
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có 2 nghiệm phân biệt:\nx1 = {x1}\nx2 = {x2}"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x = {x}"
    else:
        return "Phương trình vô nghiệm (không có nghiệm thực)."
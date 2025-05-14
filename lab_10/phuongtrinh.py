def bac_1(a, b):
    if a == 0:
        if b == 0:
            return "Phuong trinh vo so nghiem"
        else:
            return "Phuong trinh vo nghiem"
    else:
        x = -b//a
        return f"Phuong trinh co nghiem x = {x}"

def bac_2(a, b, c):
    if a == 0:
        return bac_1(b, c)

    delta = b*b - 4*a*c
    if delta < 0:
        return "Phuong trinh vo nghiem"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phuong trinh co nghiem kep x = {x}"
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return f"Phuong trinh co hai nghiem phan biet: x1 = {x1}, x2 = {x2}"
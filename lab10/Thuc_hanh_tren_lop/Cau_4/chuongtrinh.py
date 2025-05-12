import math
def bacnhat(a,b):
    if a==0:
        if b==0:
            return "Phuong trinh co vo so nghiem"
        else:
            return "Phuong trinh vo nghiem"
    else:
        return -b/a
def bachai(a,b,c):
    if a==0:
        return bacnhat(b,c)
    delta=b**2 - 4*a*c
    if delta<0:
        return "Phuong trinh vo nghiem"
    elif delta ==0:
        x=-b/(2*a)
        return f"Phuong trinh co nghiem kep x1=x2={x}"
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        return f"Phuong trinh co 2 nghiem phan biet: x1={x1}, x2={x2}"
    
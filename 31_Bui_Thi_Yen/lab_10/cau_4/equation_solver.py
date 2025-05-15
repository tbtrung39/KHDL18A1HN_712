import math

def solve_linear_equation(a, b):
    """
    Giải phương trình bậc nhất: ax + b = 0
    Trả về nghiệm hoặc thông báo vô nghiệm/vô số nghiệm
    """
    if a == 0:
        if b == 0:
            return "Phương trình có vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        return -b / a

def solve_quadratic_equation(a, b, c):
    """
    Giải phương trình bậc hai: ax² + bx + c = 0
    Trả về nghiệm hoặc thông báo về số nghiệm
    """
    if a == 0:
        return solve_linear_equation(b, c)
    
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return "Phương trình vô nghiệm thực"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
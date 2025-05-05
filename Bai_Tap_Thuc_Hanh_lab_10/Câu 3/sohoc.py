def Ucln(a, b):
    """Trả về ước chung lớn nhất (GCD) của hai số nguyên a và b"""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def Bcnn(a, b):
    """Trả về bội chung nhỏ nhất (LCM) của hai số nguyên a và b"""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // Ucln(a, b)
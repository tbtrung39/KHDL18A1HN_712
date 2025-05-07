def nhap_so_nguyen():
    n=input("Nhap 1 so nguyen: ")
    while not (n.isdigit() or (n.startswith('-') and n[1:].isdigit())):
        print("Khong hop le")
        n=input("Nhap 1 so nguyen: ")
    return int(n)
def nhiphan(n):
    return bin(n)[2:] if n>=0 else '-' + bin(n)[3:]
def batphan(n):
    return oct(n)[2:] if n>=0 else '-' + oct(n)[3:]
def thaplucphan(n):
    return hex(n)[2:].upper() if n>=0 else '-' +hex(n)[3:].upper()



def nhap_so_nguyen():
    n = int(input("Nhập vào một số nguyên: "))
    return n

def in_so(n):
    print(f"Số bạn vừa nhập là: {n}")

def doi_sang_nhi_phan(n):
    print(f"Số {n} trong hệ nhị phân là: {bin(n)[2:]}")

def doi_sang_bat_phan(n):

    print(f"Số {n} trong hệ bát phân là: {oct(n)[2:]}")

def doi_sang_thap_luc_phan(n):
    print(f"Số {n} trong hệ thập lục phân là: {hex(n)[2:].upper()}")
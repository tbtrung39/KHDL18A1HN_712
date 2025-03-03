def la_so_nguyen_to(n):
    
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def in_so_nguyen_to(n):
   
    ket_qua = []
    for num in range(2, n + 1):
        if la_so_nguyen_to(num):
            ket_qua.append(num)
    return ket_qua


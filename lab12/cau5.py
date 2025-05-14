try:
    n = input('n = ')
    if not n.isdigit():
        raise TypeError('n phai la so nguyen')
    n = int(n)
    if n < 1:
        raise ValueError('n phai la so nguyen duong > 0')
    
    def S1(n: int):
        if n == 1: return 1
        return n + S1(n - 1)
    def S2(n: int):
        if n == 1: return 1
        return n**2 + S1(n - 1)
    
    print('S1 =', S1(n))
    print('S2 =', S2(n))
    
except Exception as e:
    print('*', e)
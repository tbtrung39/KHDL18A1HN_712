# Câu 11. Cài đặt thuật toán kiểm tra số nguyên tố Miller-Rabin. 
# Biết đối với điều kiện Miller-Rabin giả sử n là một số cần kiểm tra, n phải thỏa mãn
# - n là số lẻ và lớn hơn 2.
# - Nếu n là số chẵn khác 2, nó không phải số nguyên tố.
# - Với một số nguyên ngẫu nhiên a (2 ≤ a ≤ n−2) thì (a^(n-1) – 1) % n == 0

import random
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result
def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = mod_exp(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True
n = int(input("Nhập một số nguyên: "))
if miller_rabin(n):
    print(n, "là số nguyên tố.")
else:
    print(n, "không phải là số nguyên tố.")

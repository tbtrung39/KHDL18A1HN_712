# Câu 15. Cài đặt thuật toán kiểm tra số nguyên tố Miller-Rabin. Biết đối với điều kiện Miller-Rabin giả sử n là một số cần kiểm tra, n phải thỏa mãn:
# - n là số lẻ và lớn hơn 2.
# - Nếu n là số chẵn khác 2, nó không phải số nguyên tố.
# - Với một số nguyên ngẫu nhiên a (2 ≤ a ≤ n−2) thì (a^(n-1) – 1) % n == 0

import random
def power_mod(a, b, mod):
    result = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        b = b // 2
        a = (a * a) % mod
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
        x = power_mod(a, d, n)        
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = power_mod(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
n = int(input("Nhập số cần kiểm tra: "))

if miller_rabin(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")

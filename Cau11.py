# Câu 11. Cài đặt thuật toán tìm nghiệm nguyên của phương trình ax ≡ b (mod m) (nhập vào a, b, m). Biết phương trình có nghiệm khi và chỉ khi ước chung lớn nhất (UCLN) của a và m chia hết cho b.

import math
def ucln(a, m):
    return math.gcd(a, m)
def tim_nghiem(a, b, m):
    ucln_val = ucln(a, m)
    if b % ucln_val != 0:
        return "Phương trình vô nghiệm."
    a_prime = a // ucln_val
    b_prime = b // ucln_val
    m_prime = m // ucln_val
    for x in range(m_prime):
        if (a_prime * x) % m_prime == b_prime:
            return x  
    return "Phương trình vô nghiệm."
a = int(input())
b = int(input())
m = int(input())
result = tim_nghiem(a, b, m)
print(result)

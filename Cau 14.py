# Câu 14. Cài đặt thuật toán tìm nghiệm nguyên của phương trình ax ≡ b (mod m) (nhập vào a, b, m). Biết phương
# trình có nghiệm khi và chỉ khi ước chung lớn nhất (UCLN) của a và m chia hết cho b

def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def euclid_mo_rong(a, m):
    t, new_t = 0, 1
    r, new_r = m, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None 
    if t < 0:
        t = t + m
    return t
def tim_nghiem(a, b, m):
    g = ucln(a, m)
    if b % g != 0:
        return None  

    a, b, m = a // g, b // g, m // g
    x0 = euclid_mo_rong(a, m)
    if x0 is None:
        return None  
    x = (x0 * b) % m
    return x
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
m = int(input("Nhập m: "))
nghiem = tim_nghiem(a, b, m)
if nghiem is None:
    print("Phương trình không có nghiệm.")
else:
    print(f"Nghiệm nguyên của phương trình là x = {nghiem}")

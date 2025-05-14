# Câu 14. Tìm số nguyên dương nhỏ nhất x thỏa mãn đồng dư x ≡ a (mod m) và x ≡ b (mod n).

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
def tim_x(a, m, b, n):
    k = 0
    while (a + k * m) % n != b % n:
        k += 1
    return a + k * m
a = int(input("Nhập a: "))
m = int(input("Nhập m: "))
b = int(input("Nhập b: "))
n = int(input("Nhập n: "))
x = tim_x(a, m, b, n)
print(f"Số nguyên dương nhỏ nhất x thỏa mãn đồng dư là: {x}")

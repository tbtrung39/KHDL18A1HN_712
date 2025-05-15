def s1(n):
    if n == 1:
        return 1
    return n + s1(n - 1)

def s2(n):
    if n == 1:
        return 1
    return n**2 + s2(n - 1)

try:
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        raise ValueError("n phải là số nguyên dương lớn hơn 0")
    print("S1 =", s1(n))
    print("S2 =", s2(n))
except ValueError as ve:
    print("Lỗi giá trị:", ve)
except RecursionError:
    print("Lỗi: Quá sâu trong đệ quy, n quá lớn!")
except Exception as e:
    print("Lỗi khác:", e)

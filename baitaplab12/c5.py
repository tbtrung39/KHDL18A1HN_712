def tong_S1(n):
    if n == 1:
        return 1
    return n + tong_S1(n - 1)

def tong_S2(n):
    if n == 1:
        return 1
    return n**2 + tong_S2(n - 1)

while True:
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n <= 0:
            raise ValueError("n phải là số nguyên dương.")
        
        s1 = tong_S1(n)
        s2 = tong_S2(n)

        print(f"S1 = 1 + 2 + ... + {n} = {s1}")
        print(f"S2 = 1² + 2² + ... + {n}² = {s2}")
        break  # Kết thúc nếu nhập đúng
    except ValueError as e:
        print("Lỗi:", e)

try:
    n = int(input("Nhập n: "))
    if n <= 0:
        raise ValueError("n phải là số nguyên dương.")
    s1 = sum(range(1, n+1))
    s2 = sum(i**2 for i in range(1, n+1))
    print(f"S1 = {s1}, S2 = {s2}")
except ValueError as e:
    print("Loi:", e)

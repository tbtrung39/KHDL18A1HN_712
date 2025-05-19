try:
    n = int(input("nhap n: "))
    if n < 0:
        raise ValueError("n phai la so nguyen duong")
    s1 = sum(range(1,n+1))
    s2 = sum(i**2 for i in range(1,n+1))
    print(f"s1 = {s1}","s2 = {s2}")
except ValueError as e:
    print("loi", e)
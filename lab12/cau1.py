try:
    a, b, c = map(float, input("Nhập 3 cạnh a b c: ").split())
    print("Là tam giác." if a + b > c and a + c > b and b + c > a else "Không phải tam giác.")
except:
    print("Loi.")
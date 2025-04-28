#Câu 1:
def max2(a,b):
    if a > b:
        return a
    else:
        return b
def max3(a, b, c):
    return max2(max2(a, b), c)
a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai: "))
c = int(input("Nhap so thu ba: "))
print(f"So lon nhat trong 3 so {a}, {b}, {c} la so: ", max3(a, b, c))

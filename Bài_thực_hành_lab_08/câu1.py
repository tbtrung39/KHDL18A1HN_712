def value(x):
    return x + 1

def count(x):
    print("Số kế tiếp là:", value(x))

n = int(input("Nhập một số nguyên: "))
count(n)

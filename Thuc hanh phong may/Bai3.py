import sohoc

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
n = int(input("Nhập số nguyên dương n để tính tổng ước: "))

print("UCLN của", a, "và", b, "là:", sohoc.Ucln(a, b))
print("BCNN của", a, "và", b, "là:", sohoc.Bcnn(a, b))
print("Tổng các ước của", n, "là:", sohoc.SumDivisor(n))

import sohoc
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
n = int(input("Nhập số nguyên n: "))

print("UCLN của: ", a, " va ", b, " la: ", sohoc.Ucln(a, b))
print("BCNN của: ", a, " va ", b, " la: ", sohoc.Bcnn(a, b))
print("Tổng các ước của: ", a, " va ", b, " la: ", sohoc.SumDivisor(n))
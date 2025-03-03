n = int(input("Nhập số n: "))
s = 0
for i in range(1, n+1):
    s = 2*(i+1)/(2*i+3)
print("Kết qủa", round(s,3))
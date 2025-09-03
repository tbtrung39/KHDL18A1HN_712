t=int(input("nhap thoi gian tham nien(thang): "))
luongcn=1350000
if t<12 and t>0:
    luong=luongcn*2.34
elif t>=12 and t<36:
    luong=luongcn*3.33
elif t>=36 and t<60:
    luong=luongcn*3.66
elif t>=60:
    luong=luongcn*3.99
print("luong theo tham nien la: ",luong)


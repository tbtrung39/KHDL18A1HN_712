#Bài 2
d=int(input("nhập số ngày: "))
h=int(input("nhập số giờ: "))
m=int(input("nhập số phút: "))
s=int(input("nhập số giây: "))
if s>=60:
    t1=s//60
    m+=t1
    s-=(60*t1)
if m>=60:
    t2=m//60
    h+=t2
    m-=(60*t2)
if h>=24:
    t3=h//24
    d+t3
    h-=(24*t3)
print(d,"ngày",h,"giờ",m,"phút",s,"giây")

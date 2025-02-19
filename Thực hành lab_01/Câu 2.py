#Câu 2 :
s = int(input("Nhập giây:"))
d = s//(24*3600)
s %= (24*3600)
h = s//3600
s %= 3600
m = s // 60
s %= 60
print(d,"ngày",h,"giờ",m,"phút",s,"giây")
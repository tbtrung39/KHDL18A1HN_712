chu_so = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
num = input("Nhap mot so nguyen duong: ")
chuoi_chu = chu_so[int(num[0])]

for a in num[1:]:
    chuoi_chu += " " + chu_so[int(a)]
print("dang chu: ", chuoi_chu)
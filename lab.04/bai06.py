# Cau 6.
chu_so = ["Khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
num = input("Nhap mot so nguyen duong: ")
chuoi_chu = chu_so[int(num[0])]

for c in num[1:]:
    chuoi_chu += " " + chu_so[int(c)]
print("Dang chu: ", chuoi_chu)
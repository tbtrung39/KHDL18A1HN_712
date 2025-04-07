#Câu 1:
a=set()
while True:
    ky_tu=(input("Nhap ky tu:"))
    if ky_tu=="ESC":
        break
    a.add(ky_tu)
so=set()
for c in a:
    if not c.isdigit():
        so.add(c)
if not so:
    print()
else: print("số phần tử còn lại sau khi xóa ký tự số khỏi tập hợp là:",len(so))

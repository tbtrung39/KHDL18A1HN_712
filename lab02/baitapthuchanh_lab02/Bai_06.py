so = int(input("Nhập số nguyên có ba chữ số: "))
tram = so // 100
chuc = (so // 10) % 10
don_vi = so % 10
print(tram, "trăm", end=" ")
if chuc == 0 and don_vi != 0:
    print("lẻ", don_vi)
elif chuc == 1:
    print("mười", don_vi if don_vi != 0 else "")
else:
    print(chuc, "mươi", don_vi if don_vi != 0 else "")

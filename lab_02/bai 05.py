so = input("Nhập một số nguyên: ")

chu_so = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]

for c in so:
    if c.isdigit():
        print(chu_so[int(c)], end=" ")
    else:
        print("Không hợp lệ!", end=" ")
print()

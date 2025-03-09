so = input("Nhap mot so thap phan: ")
chu_so_text = ["Khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
print("Dang chu", end = " ")
i = 0
while i < 1:
    j = 0
    while j < len(so):
        if so[j] == ".":
            print("play", end = " ")
        else:
            print(chu_so_text[int(so[j])], end = " ")
        j += 1
    i += 1
print()
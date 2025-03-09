so = input("Nhập một số nguyên: ").strip()
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
i = 0
if so[0] == "-":
    print("âm", end=" ")
    i = 1  
while i < len(so):
    print(chu_so[int(so[i])], end=" ")
    i += 1
print()
n = input("Nhập số có 4 chữ số: ")
chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

i = 0
while i < len(n):
    so = int(n[i])
    print(chu[so], end=" ")
    i = i + 1
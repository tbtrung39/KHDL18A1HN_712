print("Nhập đoạn văn bản (kết thúc bằng dòng trống):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

van_ban = "\n".join(lines)
tu_don = input("Nhập từ đơn cần đếm: ").strip()
tu_trong_van_ban = van_ban.split()
so_lan = 0
for tu in tu_trong_van_ban:
    if tu == tu_don:
        so_lan += 1

print(f"Từ đơn '{tu_don}' xuất hiện {so_lan} lần trong đoạn văn.")

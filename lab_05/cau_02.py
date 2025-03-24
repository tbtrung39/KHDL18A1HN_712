chuoi = input("Nhập chuỗi: ")

dem = 0

for ky_tu in chuoi:
    if not (('a' <= ky_tu <= 'z') or ('A' <= ky_tu <= 'Z') or ('0' <= ky_tu <= '9')):
        dem += 1

print("Số ký tự không phải chữ cái và không phải số là:", dem)

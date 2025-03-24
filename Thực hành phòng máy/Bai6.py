Str = input("Nhập chuỗi Hex: ")
hop_le = True
for ky_tu in Str:
    if not (ky_tu.isdigit() or ('A' <= ky_tu <= 'F') or ('a' <= ky_tu <= 'f')):
        hop_le = False
        break
if not hop_le:
    print("Chuỗi không hợp lệ trong hệ Hex.")
else:
    so_thap_phan = int(Str, 16)
    print("Chuỗi hợp lệ trong hệ Hex.")
    print("Giá trị thập phân là:", so_thap_phan)

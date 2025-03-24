chuoi = input("Nhập chuỗi cần kiểm tra hệ Hex: ")

hex_hop_le = "0123456789ABCDEFabcdef"

chuoi_hex = ""
for ky_tu in chuoi:
    if ky_tu in hex_hop_le:
        chuoi_hex += ky_tu

if chuoi_hex == "":
    print("Không có ký tự nào thuộc hệ Hex!")
else:
    print("Chuỗi hợp lệ trong hệ Hex là:", chuoi_hex)
    so_thap_phan = int(chuoi_hex, 16)
    print("Giá trị thập phân tương ứng là:", so_thap_phan)

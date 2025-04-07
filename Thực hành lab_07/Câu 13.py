#Câu 13:
chuoi = input("Nhập chuỗi ký tự: ")
dict_ky_tu = {}
for ky_tu in chuoi:
    if ky_tu in dict_ky_tu:
        dict_ky_tu[ky_tu] += 1
    else:
        dict_ky_tu[ky_tu] = 1
for ky_tu, so_lan in dict_ky_tu.items():
    print(f"'{ky_tu}': {so_lan}")

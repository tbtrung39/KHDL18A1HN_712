str_input = input("Nhập đoạn văn bản: ")
tudon = input("Nhập từ cần tìm: ")
str_input_lower = str_input.lower()
tudon_lower = tudon.lower()

danhsach_tu = str_input_lower.split()
so_lan = danhsach_tu.count(tudon_lower)

print(f"Từ '{tudon}' xuất hiện {so_lan} lần trong đoạn văn bản.")

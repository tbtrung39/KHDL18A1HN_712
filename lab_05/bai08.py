str_input = input('Nhập đoạn văn bản: ')
tu = input('Nhập từ cần tìm: ')

danhsach_tu = str_input.lower().split()
so_lan = danhsach_tu.count(tu.lower())

print(f'Từ "{tu}" xuất hiện {so_lan} lần trong đoạn văn bản')

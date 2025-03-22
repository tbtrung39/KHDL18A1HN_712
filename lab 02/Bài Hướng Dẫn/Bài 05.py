print('Nhập ký tự :', end='')
ky_tu = input()

if ky_tu.lower() in ('a', 'e', 'i', 'o', 'u'):
    print("Ký tự '", ky_tu, "' là nguyên âm!")
else:
    print("Ký tự '", ky_tu, "' là phụ âm!")
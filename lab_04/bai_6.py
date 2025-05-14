chu_so = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']
num = input('Nhập một số nguyên dương: ')
chuoi_chu = chu_so[int(num[0])]

for c in num[1:]:
    chuoi_chu += ' ' + chu_so[int(c)]
print('Dạng chữ: ', chuoi_chu)
s = input("Nhập : ")
tu = ""
for c in s:
    if c != ' ' and c != ',':
        tu += c
    else:
        if tu != '':
            print(tu)
            tu = ''
if tu != '':
    print(tu)
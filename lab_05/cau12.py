S1 = input("Nhập chuỗi ký tự: ")
for ky_tu in [',', '\n']:
    S1 = S1.replace(ky_tu, ' ')
tu = S1.split()
for t in tu:
    print(t)

try:
    with open(input("Nhập tên file: "), 'r', encoding='utf-8') as f:
        open("copy.dat", 'w', encoding='utf-8').write(f.read())
    print("Đã sao chép vào copy.dat")
except:
    print("Loi.")

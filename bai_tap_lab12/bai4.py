try:
    a, b = input("File nguồn và đích: ").split()
    open(b, 'w', encoding='utf-8').write(open(a, 'r', encoding='utf-8').read())
    print("Đã sao chép.")
except:
    print("Loi.")

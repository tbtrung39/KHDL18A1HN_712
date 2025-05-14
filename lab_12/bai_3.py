try:
    f = input('Nhap ten tap tin: ')
    with open(f, 'r') as file:
        data = file.read()
        file.close()
        with open('copy.dat', 'w') as file1:
            file1.write(data)
            file1.close()
except FileNotFoundError as e:
    print('* Khong tim thay file ten:', f)
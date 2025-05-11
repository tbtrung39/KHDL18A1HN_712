def sap_xep_day_so(path):
    with open(path, 'r') as file:
        numbers = list(map(int, file.read().split()))

    numbers.sort()

    with open('out.dat', 'w') as file:
        file.write(' '.join(map(str, numbers)))
path=input('nhập đường dẫn đến file nội dung muốn đọc nội dung : path= ')
sap_xep_day_so(path)

def tao_file_mau():
    with open('Inp.txt', 'w') as f:
        f.write("10 5 8 2 1 4 9 6 3 7")

# Đọc, sắp xếp và ghi ra file
def sap_xep_tang_dan(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read().strip().split()
        numbers = list(map(int, data))
        numbers.sort()  # sắp xếp tăng dần
    
    with open(output_file, 'w') as f:
        f.write(' '.join(map(str, numbers)))
tao_file_mau()
sap_xep_tang_dan('Inp.txt', 'out.dat')
print("Đã sắp xếp và ghi kết quả vào 'out.dat'.")

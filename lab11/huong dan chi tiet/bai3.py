def read_data_file(file_path):
    A = []
    with open(file_path,'r') as file:
        for line in file:
            num = int(line.strip())
            A.append(num)
    return A
path = input("Nhap duongdan den file muon nhap noi dung: path=")
A = read_data_file(path)
print(A)
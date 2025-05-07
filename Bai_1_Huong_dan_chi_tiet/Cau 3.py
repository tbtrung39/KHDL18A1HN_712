# Cau 3.Dvq
def read_data_file(file_path):
    A=[]
    with open(file_path, 'r') as file:
        for line in file:
            num=int(line.strip())
            A.append(num)
    return A
path=input("Nhap duong dan dan den file muon doc noi dung :path=")
A=read_data_file(path)
print(A)
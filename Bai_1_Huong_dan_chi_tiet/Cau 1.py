# Cau 1. Dvq 
def read_data_from_file(path):
    with open(path, 'r') as file:
        n=int(file.readline().strip())
        numbers=[]
        numbers.append(n)
        numbers+=list(map(float,file.readline().strip().split()))
        return numbers
print('')
path=input("Nhap duong dan den file muon doc noi dung :path=")
print("Du lieu doc duoc la:",read_data_from_file(path))
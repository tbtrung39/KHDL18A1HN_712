# Cau 2.Dvq
def read_fin_file(file_path):
    with open(file_path,'r') as fin:
        n=int(fin.readline())
        numbers=[]
        total_sum=0
        for i in range(n):
            line=fin.readline().strip().split()
            line_sum=sum(map(float,line))
            numbers.append(line_sum)
            total_sum+=line_sum
    with open('Bai_1_Huong_dan_chi_tiet/found.dat','w') as found:
        found.write(str(total_sum) + '\n')
        for i in range(n):
            found.write(str(numbers[i]) + '\n')
path=input("nhap duong dan file muon doc noi dung :path=")
read_fin_file(path)
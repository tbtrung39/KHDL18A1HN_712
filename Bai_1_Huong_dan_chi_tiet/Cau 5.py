# Cau 5.Dvq
def write_matrix_to_file(A, filename):
    with open(filename,'w') as file:
        m = len(A)
        n = len(A[0])
        file.write(f"{m} {n}\n")
        for row in A:
            file.write(' '.join(map(str,row)) + '\n')
A=[[1,2,3],[4,5,6],[7,8,9]]
filename="Bai_1_Huong_dan_chi_tiet/matrix.txt"
write_matrix_to_file(A,filename)
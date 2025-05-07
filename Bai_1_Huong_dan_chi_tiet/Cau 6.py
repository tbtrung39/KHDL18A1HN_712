# Cau 6.Dvq
def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        m, n = map(int,file.readline().strip().split())
        print('Ma tran co',m, 'dong', n, 'cot')
        A=[]
        for i in range(m):
            row = list(map(float,file.readline().strip().split()))
            A.append(row)
        return A
print("Nhap vao duong dan va ten file can doc",end='')
filename = input(":")
A = read_matrix_from_file(filename)
print("Du lieu doc tu file '",filename,"' duoc chuyen tu ma tran vao danh sach A:")
print(A)
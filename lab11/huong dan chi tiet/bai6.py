def read_matrix_to_file(A,filename):
    with open(filename, 'r') as file:
        m,n = map(int,file.readline().strip().split())
        print('Ma tran co',m,'dong',n,'cot')
        A =[]
        for i in range(m):
            row= list(map(float,file.readline().strip().split()))
            A.append(row)
        return A
print("Nhap vao duongdan vaten file can doc",end= ' ')
filename=input(":")
A = read_matrix_to_file(filename)
print("Du lieu doc tu file'",filename,"'duoc chuyen tu Ma tran vao danh sach A :")
print(A)           
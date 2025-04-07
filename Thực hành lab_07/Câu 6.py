#Câu 6:
n=int(input("Nhập số tự nhiên n: "))
snt=[]
so_hien_tai = 2
while len(snt)<n:
    la_snt= True
    for i in range(2,int(so_hien_tai**0.5)+1):
        if so_hien_tai%i==0:
            la_snt=False
            break
    if la_snt:
        snt.append(so_hien_tai)
    so_hien_tai+=1
print(f"{n} số nguyên tố đầu tiên",snt)
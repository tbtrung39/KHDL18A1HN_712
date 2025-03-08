#Câu 3:
x=float(input('Nhập x:'))
n=0
cos_x=1
term=1
while abs(term)>1e-4:
    term*=-x**2/((2*n+1)*2*n+2)
    cos_x+=term
    n+=1
print("Giá trị gần đúng của cos(x):", cos_x)
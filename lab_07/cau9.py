n=int(input("Nhập số tự nhiên n:"))
A=set()
B=set()
for i in range(2,n):
    snt=True
    for j in range(2,i):
        if i%j==0:
            snt=False
            break
    if snt and n%i==0:
        A.add(i)
    elif snt and n%i!=0:
        B.add(i)
print("Tập các số nguyên tố là ước của n:A",A)
print("Tập các số nguyên tố nhỏ hơn n và không là ước của n: B",B)
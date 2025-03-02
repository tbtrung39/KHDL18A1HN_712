#Câu 4:
n=int(input("Nhập số nguyên n:"))
if n <=1 :
    print("Không có số nguyên tố nào nhỏ hơn hoặc bằng ",n)
else:
    for i in range(2,n+1):
        for k in range(2,int(i**0.5)+1):
            if i%k==0:
                break
        else:
            print(i)
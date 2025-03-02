#Câu 10:
h = int(input("Nhập độ cao của tam giác: "))
#a)
for i in range(h):
    for j in range(h - i - 1):
        print(" ", end="")  
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == h - 1:
            print("*", end="")  
        else:
            print(" ", end="")  
    print() 
#b)
ngoai=h-1
trong=1
for t in range(h):
    if t==0 : 
        print(ngoai*" "+"*")
    elif t<h-1:
        print(ngoai*" "+"*"+trong*" "+"*")
        trong+=2
    else:
        print("* "*h)
    ngoai-=1
#c)
khoang_ngoai=h-1
so_luong_sao=1
for k in range(h):
    print(khoang_ngoai*" ",so_luong_sao*"* ")
    khoang_ngoai-=1
    so_luong_sao+=1
    

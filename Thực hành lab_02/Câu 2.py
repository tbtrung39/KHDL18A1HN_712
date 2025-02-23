#Câu 2 : ax^2 + bx + c = 0
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if a==0 and b!=0 :
    print("phương trình là phương trình bậc nhất có nghiệm là x =",-c/b)
elif a==0 and b==0 :
    print("phương trình vô nghiệm")
elif a!=0 :
    delta = b**2 - 4*a*c
    if delta == 0 :
        print("phương trình có nghiệm kép x =",-b/(2*a))
    elif delta < 0 :
        print("phương trình vô nghiệm")
    elif delta > 0 :
        print("phương trình có 2 nghiệm phân biệt x1 =",(-b+(delta)**(1/2))/(2*a),"và x2 =",(-b-(delta)**(1/2))/(2*a))
        

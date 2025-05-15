import math
def tam_giac():
    lst = []
    try:
        a, b, c = map(int,input("Nhap do dai a, b, c: ").split())
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError ("Canh tam giac khong the am")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError ("Khong du dk thanh 1 tam giac")
        else:
            lst.append(a)
            lst.append(b)
            lst.append(c)
            print(lst)
            p = (a+b+c)/2
            s =  math.sqrt(p*(p-a)*(p-b)*(p-c))
            print(s)
    except ValueError as e:
        print("Loi: ",e)

tam_giac()
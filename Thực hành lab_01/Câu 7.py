#Câu 7: ax^2 + bx + c = 0
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
x_dinh = -b/(2*a)
y_dinh = a*(x_dinh)**2 + b*x_dinh + c
print("Tọa độ đỉnh của phương trình là: (","%0.2f"%(x_dinh),",","%0.2f"%(y_dinh),")")

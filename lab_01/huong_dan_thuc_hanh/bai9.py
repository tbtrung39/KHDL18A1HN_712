a, b, c = map(float,input("Xin mời nhập độ dài 3 cạnh: ").split())
chuvi = a + b + c
p = chuvi/2;
import math
dientich = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"Vhu vi của tam giác là {chuvi:.2f}")
print(f"Diện tích của tam giác là {dientich:.2f}")
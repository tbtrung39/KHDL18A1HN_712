#Câu 3:
import random
n=float(input("Nhập số thực:"))
A=set()
a=float(input("Nhập giá trị nhỏ nhất a:"))
b=float(input("Nhập giá trị lớn nhất b:"))
while len(A)<n:
    A.add(random.uniform(a,b))
print("Phần tử lớn nhất của tập A:",min(A))
print("Phần tử lớn nhất của tập A:",max(A))
print("tổng các phần tử của tập hợp A:",sum(A))

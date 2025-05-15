# Câu 11
import random  
n = int(input("Nhap so luong phan tu: "))  
#   
A = [int(input(f"Nhap so thu {i+1}: ")) for i in range(n)]  
# 
B = [x for x in A if x % 3 == 0 and x % 5 != 0]  
print("Danh sach B:", B)  
#   
C = [x**2 for x in A]  
print("Danh sach C:", C)  
#   
D = random.sample([x for x in A if x % 3 == 0], min(len([x for x in A if x % 3 == 0]), n))  
print("Danh sach D:", D)
#Câu a
def tinh_tong_a(n):
    if n == 1:
        return 1 / (1*2)
    return 1 / (n*(n+1)) + tinh_tong_a(n-1)

n = int(input("Nhập n cho biểu thức a: "))
print("Tổng S =", tinh_tong_a(n))

#Câu b
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n-1)
def tinh_tong_b(n):
    if n == 1:
        return 1
    return 1 / giai_thua(n) + tinh_tong_b(n-1)

n= int(input("Nhập n cho biểu thức b : "))
print("Tổng S = ",tinh_tong_b(n))

#Câu c
import math
def tinh_bieu_thuc_c(n):
    if n == 1:
        return math.sqrt(3)
    return math.sqrt(3*n+tinh_bieu_thuc_c(n-1))

n = int(input("Nhập n cho biểu thức c : "))
print("Giá trị S = ",tinh_bieu_thuc_c(n))

#câu d
import math
def tinh_S(n):
    if n <= 1:
        return "n phải > 1"
    inner = math.sqrt(1)
    inner = math.pow(2+inner , 1/n)
    inner = math.pow(n-1+inner,1/n)
    S = math.pow(n + inner,1/(n+1))
    return S
n = 2
print("S = ",tinh_S(n))
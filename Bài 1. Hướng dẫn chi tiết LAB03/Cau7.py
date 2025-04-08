# Cau 7.
# a.
h=int(input("Nhập chiều cao tam giác: "))

for i in range(0,h):
    for j in range(0,i+1):
        print("* ",end='')
    print("\r") 

# b.
h=int(input("Nhập giá trị chiều cao tam giác: "))
k = 2*h -2
for dong in range(1, h+1):
    for cot in range(1, k+1):
        print(end=" ")
for cot in range(1, dong+1):
    print("*", end=" ")
k=k-2
print("\r")

# c.
h=int(input('Nhập chiều cao tam giác số :'))
num = 1
for dong in range(1, h+1):
    num = 1
for cot in range(1, dong+1):
    print(num, end=" ")
num = num + 1
print("\r")

# d.
h=int(input("Nhập giá trị chiều cao tam giác cân: "))
k = 2*h -2
for dong in range(1, h+1):
    for cot in range(1, k+1):
        print(end=" ")
print("*", end=" ")
k=k-1
print("\r")

# d.
num = 65
h=int(input('Nhập chiều cao tam giác ký tự: ') )
for i in range(0, h):
    for j in range(0, i+1):
        ch = chr(num)
print(ch, end=" ")
num = num + 1
print("\r")
A = set(map(int,input("Nhập số thứ tự của các sinh viên thi C++").split()))
B = set(map(int,input("Nhập số thứ tự của các sinh viên thi java").split()))
C = set(map(int,input("nhập số thứ tự các sinh vien thi python").split()))
x = (A^B^C)-(A&B&C)-(A&B)-(B&C)
print("Danh sách số thứ tự của thí sinh thi 1 năm la:",x)
y = (A&B)|(A&C)|(B&C)-(A&B&C)
print("Danh sách số thứ tự của thi sinh 2 năm là:",y)
z = A&B&C
print("Danh sách số thứ tự của thí sinh thi cae 2 năm la:",z)
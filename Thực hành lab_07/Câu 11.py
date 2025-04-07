#Câu 11:
A=set(map(int,input("Nhập số thứ tự của các sinh viên thi C++:").split()))
B=set(map(int,input("Nhập số thứ tự của các sinh viên thi Java:").split()))
C=set(map(int,input("Nhập số thứ tự của các sinh viên thi Python:").split()))
x=(A^B^C)-(A&B&C)-(A&B)-(A&C)-(B&C)
print("danh sách số thứ tự của thí sinh thi 1 môn là:",x)
y=(A&B)|(A&B)|(B&C)-(A&B&C)
print("danh sách số thứ tự của thí sinh thi 2 môn là:",y)
z=A&B&C
print("danh sách số thứ tự của thí sinh thi cả 3 môn là:",z)

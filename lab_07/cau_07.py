a = input("Nhập các ký tự cho A (không cách): ")
b = input("Nhập các ký tự cho B (không cách): ")

A = set(a)
B = set(b)
C = A & B  

print("Phần tử chung của A và B:", C)

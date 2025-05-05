A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")

found = False
for i in range(1, len(A)):
    a1 = int(A[:i])
    a2 = int(A[i:])
    if a1 + a2 == int(B):
        print(f"{a1}+{a2}={B}")
        found = True
        break

if not found:
    print("Không tồn tại cách đặt!")
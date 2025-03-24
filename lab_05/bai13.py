A = input("Nhập chuỗi ký tự A: ")
B = input("Nhập chuỗi ký tự B: ")
found = False
for i in range(1, len(A)):
    C, D = A[:i], A[i:]
    for j in range(1, len(B)):
        E, F = B[:j], B[j:]
        if int(C) + int(D) == int(E) + int(F):
            print(f"{C}+{D}={E}+{F}")
            found = True
            break
    if found:
        break
if not found:
    print("Không tồn tại cách đặt!")
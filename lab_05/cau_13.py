A = input("Nhập chuỗi A (toàn chữ số): ")
B = input("Nhập chuỗi B (toàn chữ số): ")

found = False

for i in range(1, len(A)):
    C = int(A[:i])
    D = int(A[i:])

    for j in range(1, len(B)):
        E = int(B[:j])
        F = int(B[j:])

        if C + D == E + F:
            print(f"{C}+{D} = {E}+{F}")
            found = True
            break
    if found:
        break

if not found:
    print("Không tồn tại cách đặt!")

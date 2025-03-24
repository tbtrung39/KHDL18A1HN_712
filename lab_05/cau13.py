A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")
tim_duoc = False

for i in range(1, len(A)):
    for j in range(1, len(B)):
        C = int(A[:i])
        D = int(A[i:])
        E = int(B[:j])
        F = int(B[j:])
        if C + D == E + F:
            print("Tìm được biểu thức:", C, "+", D, "=", E, "+", F)
            tim_duoc = True
            break
    if tim_duoc:
        break

if not tim_duoc:
    print("Không tồn tại cách đặt!")

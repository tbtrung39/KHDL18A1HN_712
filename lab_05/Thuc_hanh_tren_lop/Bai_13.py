chuoi_A = input("Nhập chuỗi A: ")
chuoi_B = input("Nhập chuỗi B: ")
tim_duoc = False
for i in range(1, len(chuoi_A)):
    for j in range(1, len(chuoi_B)):
        A1 = chuoi_A[:i]
        A2 = chuoi_A[i:]
        B1 = chuoi_B[:j]
        B2 = chuoi_B[j:]
        if A1.isdigit() and A2.isdigit() and B1.isdigit() and B2.isdigit():
            if int(A1) + int(A2) == int(B1) + int(B2):
                print(f"{A1} + {A2} = {B1} + {B2}")
                tim_duoc = True
                break
    if tim_duoc:
        break
if not tim_duoc:
    print("Không có cách đặt hợp lệ.")
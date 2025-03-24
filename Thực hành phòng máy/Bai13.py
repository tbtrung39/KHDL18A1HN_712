A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")

tim_duoc = False

for i in range(1, len(A)):
    for j in range(1, len(B)):
        A1 = A[:i]
        A2 = A[i:]
        B1 = B[:j]
        B2 = B[j:]

        try:
            tong1 = int(A1) + int(B1)
            so_2 = int(A2) * (10 ** len(B2)) + int(B2)

            if tong1 == so_2:
                print(f"{A1} + {B1} = {A2}{B2}")
                tim_duoc = True
                break
        except:
            continue

    if tim_duoc:
        break

if not tim_duoc:
    print("Không tồn tại cách đặt!")

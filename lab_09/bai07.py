def tim_bo_nghiem(n, tong, ket_qua=[]):
    if n == 1:
        ket_qua.append(tong)
        print(ket_qua)
        ket_qua.pop()
    else:
        for i in range(1, tong - n + 2):  
            ket_qua.append(i)
            tim_bo_nghiem(n - 1, tong - i, ket_qua)
            ket_qua.pop()

N = int(input("Nhập tổng N: "))
n = int(input("Nhập số lượng số hạng n: "))
tim_bo_nghiem(n, N)

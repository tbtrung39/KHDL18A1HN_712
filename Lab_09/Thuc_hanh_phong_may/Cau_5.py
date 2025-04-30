def sinh_hoan_vi(mang, dau, cuoi, ket_qua):
    if dau == cuoi:
        ket_qua.append(mang.copy())
    else:
        for i in range(dau, cuoi + 1):
            mang[dau], mang[i] = mang[i], mang[dau]
            sinh_hoan_vi(mang, dau + 1, cuoi, ket_qua)
            mang[dau], mang[i] = mang[i], mang[dau]

n = int(input("Nhập n: "))
mang = list(range(1, n + 1))
ket_qua = []
sinh_hoan_vi(mang, 0, n - 1, ket_qua)
print("Các hoán vị:", ket_qua)
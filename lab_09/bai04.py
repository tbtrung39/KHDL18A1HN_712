def sinh_hoan_vi(chua_dung, ket_qua):
    if not chua_dung:
        print(ket_qua)
    else:
        for i in range(len(chua_dung)):
            sinh_hoan_vi(chua_dung[:i] + chua_dung[i+1:], ket_qua + [chua_dung[i]])

n = int(input("Nhập số tự nhiên n: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    danh_sach = list(range(1, n + 1))
    print(f"Các hoán vị của dãy từ 1 đến {n}:")
    sinh_hoan_vi(danh_sach, [])

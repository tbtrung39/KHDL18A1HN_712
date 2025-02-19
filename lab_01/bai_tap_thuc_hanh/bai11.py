n = int(input("Nhập số lần tung 3 xúc xắc: "))
P_ra_6 = 1/216
P_khong_ra_6 = 1 - P_ra_6 
P_it_nhat_1_lan = 1 - (P_khong_ra_6 ** n)
print(f"Xác suất có ít nhất một lần cả 3 xúc xắc ra số 6 trong {n} lần tung là: {P_it_nhat_1_lan:.2f}")
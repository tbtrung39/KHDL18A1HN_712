n =  int(input('Nhập số lần tung xúc sắc: '))
P_khong_ra_6_mot_lan = 1 - (1 / 216)
P_ich_nhat_1_lan = 1 - (P_khong_ra_6_mot_lan ** n)
print('Xác suất có ít nhất 1 lần cả 3 ra 6 trong n lần tung là: ',round(P_ich_nhat_1_lan, 2))
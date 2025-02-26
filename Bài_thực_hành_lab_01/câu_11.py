import math
n = int(input("Nhập số lần tung xúc xắc (n): "))
# Tính xác suất để cả 3 xúc xắc đều ra 6 trong một lần tung
p_3_con_6 = 1/6 * 1/6 * 1/6
# Tính xác suất để không có lần nào cả 3 xúc xắc đều ra 6 trong n lần tung
p_khong_co_3_con_6 = (1 - p_3_con_6)**n
# Tính xác suất có ít nhất 1 lần cả 3 xúc xắc đều ra 6 trong n lần tung
p_it_nhat_1_lan_3_con_6 = 1 - p_khong_co_3_con_6
# Làm tròn kết quả
p_it_nhat_1_lan_3_con_6_rounded = round(p_it_nhat_1_lan_3_con_6, 2)
print("Xác suất có ít nhất 1 lần cả 3 xúc xắc đều ra 6 trong {} lần tung là: {}".format(n, p_it_nhat_1_lan_3_con_6_rounded))
n = int(input("Nhập số lượng thí sinh: "))
dsdiem = {}
for _ in range(n):
    sbd = input("Số báo danh: ")
    ten = input("Họ tên: ")
    diem = float(input("Điểm thi: "))
    dsdiem[sbd] = (ten, diem)

tra_sbd = input("Nhập số báo danh cần tra cứu: ")
if tra_sbd in dsdiem:
    print("Họ tên:", dsdiem[tra_sbd][0])
    print("Điểm thi:", dsdiem[tra_sbd][1])
else:
    print("Không tìm thấy số báo danh.")
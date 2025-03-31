a = []
while True:
    x = int(input("Nhập phần tử (nhập 0 để dừng): "))
    if x == 0:
        break
    a.append(x)
print("Danh sách ban đầu:", a)
duong = [x for x in a if x > 0]
khac_duong = [x for x in a if x <= 0]
a = duong + khac_duong
print("Danh sách sau khi chuyển số dương lên đầu:", a)
m = int(input("Nhập số m cần chèn: "))
if len(a) >= 5:
    a.insert(4, m)
    print("Danh sách sau khi chèn m vào vị trí thứ 5:", a)
else:
    print("Danh sách không đủ 5 phần tử để chèn m.")

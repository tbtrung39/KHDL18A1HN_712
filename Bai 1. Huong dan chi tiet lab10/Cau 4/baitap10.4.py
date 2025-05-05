import hinhtron

# Nhập thông tin bán kính hình tròn
r = float(input("Nhập bán kính hình tròn: "))

# Nhập tọa độ tâm hình tròn
O = []
x = float(input("Hoành độ = "))
O.append(x)
y = float(input("Tung độ = "))
O.append(y)
Tam = tuple(O)

# Tính chu vi hình tròn
chuvi = hinhtron.get_ChuVi(r)
print("Chu vi hình tròn là:", chuvi)

# Tính diện tích hình tròn
dientich = hinhtron.get_DienTich(r)
print("Diện tích hình tròn là: %0.4f" % dientich)

# Nhập tọa độ điểm
print('Nhập tọa độ điểm A:')
A = []
a = float(input("Nhập tọa độ x của điểm A: "))
A.append(a)
b = float(input("Nhập tọa độ y của điểm A: "))
A.append(b)
diemA = tuple(A)

# Kiểm tra điểm A có nằm trong hình tròn không
if hinhtron.is_In(Tam, diemA, r):
    print("Điểm A", diemA, "nằm trong hình tròn tâm", Tam)
else:
    print("Điểm A", diemA, "không nằm trong hình tròn tâm", Tam)

# Kiểm tra điểm A có nằm ngoài hình tròn không
if hinhtron.is_Out(Tam, diemA, r):
    print("Điểm A", diemA, "nằm ngoài hình tròn tâm", Tam)
else:
    print("Điểm A", diemA, "không nằm ngoài hình tròn tâm", Tam)

# Kiểm tra điểm A có nằm trên hình tròn không
if hinhtron.is_On(Tam, diemA, r):
    print("Điểm A", diemA, "nằm trên hình tròn tâm", Tam)
else:
    print("Điểm A", diemA, "không nằm trên hình tròn tâm", Tam)

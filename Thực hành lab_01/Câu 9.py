# Câu 9 :
x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
z = float(input("Nhập tọa độ z: "))
# tính tọa độ điểm đối xứng qua Oxy
x_oxy = x
y_oxy = y
z_oxy = -z
# tính tọa độ điểm đối xứng qua Oxz
x_oxz = x
y_oxz = -y
z_oxz = z
#tính tọa độ điểm đối xứng qua Oyz
x_oyz = -x
y_oyz = y
z_oyz = z
print("Tọa độ điểm đối xứng qua mặt phẳng Oxy: (",x_oxy,",",y_oxy,",",z_oxy,")")
print("Tọa độ điểm đối xứng qua mặt phẳng Oxz: (",x_oxz,",",y_oxz,",",z_oxz,")")
print("Tọa độ điểm đối xứng qua mặt phẳng Oyz: (",x_oyz,",",y_oyz,",",z_oyz,")")
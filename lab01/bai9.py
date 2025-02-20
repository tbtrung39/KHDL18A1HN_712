#câu9
# Nhập tọa độ điểm trong không gian Oxyz
x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
z = float(input("Nhập tọa độ z: "))

doixung_oxy = (x, y, -z)

doixung_oxz = (x, -y, z)

doixung_oyz = (-x, y, z)
print(f"Tọa độ đối xứng qua mặt phẳng Oxy: {doixung_oxy}")
print(f"Tọa độ đối xứng qua mặt phẳng Oxz: {doixung_oxz}")
print(f"Tọa độ đối xứng qua mặt phẳng Oyz: {doixung_oyz}")

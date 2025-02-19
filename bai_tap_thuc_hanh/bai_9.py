x0 = float(input("Nhập tọa độ x của điểm O: "))
y0 = float(input("Nhập tọa độ y của điểm O: "))
z0 = float(input("Nhập tọa độ z của điểm O: "))
Oxy_x, Oxy_y, Oxy_z = x0, y0, -z0
Oxz_x, Oxz_y, Oxz_z = x0, -y0, z0
Oyz_x, Oyz_y, Oyz_z = -x0, y0, z0
print(f"Tọa độ điểm đối xứng qua mặt phẳng Oxy là: ({Oxy_x}, {Oxy_y}, {Oxy_z})")
print(f"Tọa độ điểm đối xứng qua mặt phẳng Oxz là: ({Oxz_x}, {Oxz_y}, {Oxz_z})")
print(f"Tọa độ điểm đối xứng qua mặt phẳng Oyz là: ({Oyz_x}, {Oyz_y}, {Oyz_z})")


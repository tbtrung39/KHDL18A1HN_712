x, y, z = map(float, input("Nhập tọa độ của điểm P(x, y, z) trong không gian Oxyz (cách nhau bởi dấu cách): ").split())
x_oxy, y_oxy, z_oxy = x, y, -z
x_oxz, y_oxz, z_oxz = x, -y, z
x_oyz, y_oyz, z_oyz = -x, y, z
print(f"Tọa độ đối xứng qua mặt phẳng Oxy: ({x_oxy:.2f}, {y_oxy:.2f}, {z_oxy:.2f})")
print(f"Tọa độ đối xứng qua mặt phẳng Oxz: ({x_oxz:.2f}, {y_oxz:.2f}, {z_oxz:.2f})")
print(f"Tọa độ đối xứng qua mặt phẳng Oyz: ({x_oyz:.2f}, {y_oyz:.2f}, {z_oyz:.2f})")

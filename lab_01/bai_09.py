x = float(input("Nhập hoành độ x: "))
y = float(input("Nhập tung độ y: "))
z = float(input("Nhập cao độ z: "))
doi_x_Oxy = x
doi_y_Oxy = y
doi_z_Oxy = -z
doi_x_Oxz = x
doi_y_Oxz = -y
doi_z_Oxz = z
doi_x_Oyz = -x
doi_y_Oyz = y
doi_z_Oyz = z
print("Điểm đối xứng qua mặt phẳng Oxy có tọa độ:")
print("%0.2f" % doi_x_Oxy)
print("%0.2f" % doi_y_Oxy)
print("%0.2f" % doi_z_Oxy)
print("Điểm đối xứng qua mặt phẳng Oxz có tọa độ:")
print("%0.2f" % doi_x_Oxz)
print("%0.2f" % doi_y_Oxz)
print("%0.2f" % doi_z_Oxz)
print("Điểm đối xứng qua mặt phẳng Oyz có tọa độ:")
print("%0.2f" % doi_x_Oyz)
print("%0.2f" % doi_y_Oyz)
print("%0.2f" % doi_z_Oyz)

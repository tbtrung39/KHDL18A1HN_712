def diem_doi_xung(x, y, z):
    return (-x, y, z), (x, -y, z), (x, y, -z)

x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
z = float(input("Nhập tọa độ z: "))

dx_Oxy, dx_Oxz, dx_Oyz = diem_doi_xung(x, y, z)

print(f"Điểm đối xứng qua mặt phẳng Oxy: {dx_Oxy}")
print(f"Điểm đối xứng qua mặt phẳng Oxz: {dx_Oxz}")
print(f"Điểm đối xứng qua mặt phẳng Oyz: {dx_Oyz}")

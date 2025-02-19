# Nhập tọa độ điểm P(x, y, z)
x = float(input("Nhập tọa độ x: "))
y = float(input("Nhập tọa độ y: "))
z = float(input("Nhập tọa độ z: "))

# Tính tọa độ đối xứng
doi_xung_Oxy = (x, y, -z)  # Đối xứng qua mặt phẳng Oxy (đảo dấu z)
doi_xung_Oxz = (x, -y, z)  # Đối xứng qua mặt phẳng Oxz (đảo dấu y)
doi_xung_Oyz = (-x, y, z)  # Đối xứng qua mặt phẳng Oyz (đảo dấu x)

# Xuất kết quả
print(f"\nĐiểm đối xứng qua mặt phẳng Oxy: {doi_xung_Oxy}")
print(f"Điểm đối xứng qua mặt phẳng Oxz: {doi_xung_Oxz}")
print(f"Điểm đối xứng qua mặt phẳng Oyz: {doi_xung_Oyz}")
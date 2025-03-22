# Nhập tọa độ điểm ban đầu
print("Nhập tọa độ điểm trong không gian Oxyz:")
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

# Tính tọa độ điểm đối xứng qua mặt phẳng Oxy
x_oxy = x
y_oxy = -y
z_oxy = -z

# Tính tọa độ điểm đối xứng qua mặt phẳng Oxz
x_oxz = x
y_oxz = -y
z_oxz = z

# Tính tọa độ điểm đối xứng qua mặt phẳng Oyz
x_oyz = -x
y_oyz = y
z_oyz = z

# In kết quả
print("\nĐiểm đối xứng qua mặt phẳng Oxy: (", end="")
print(x_oxy, end="")
print(", ", end="")
print(y_oxy, end="")
print(", ", end="")
print(z_oxy, end="")
print(")")

print("Điểm đối xứng qua mặt phẳng Oxz: (", end="")
print(x_oxz, end="")
print(", ", end="")
print(y_oxz, end="")
print(", ", end="")
print(z_oxz, end="")
print(")")

print("Điểm đối xứng qua mặt phẳng Oyz: (", end="")
print(x_oyz, end="")
print(", ", end="")
print(y_oyz, end="")
print(", ", end="")
print(z_oyz, end="")
print(")")
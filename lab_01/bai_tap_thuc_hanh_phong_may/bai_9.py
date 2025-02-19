x, y, z = map(float, input("Nhập tọa độ điểm P(x, y, z): ").split())

print(f"Tọa độ đối xứng qua Oxy: ({x}, {y}, {-z})")
print(f"Tọa độ đối xứng qua Oxz: ({x}, {-y}, {z})")
print(f"Tọa độ đối xứng qua Oyz: ({-x}, {y}, {z})")

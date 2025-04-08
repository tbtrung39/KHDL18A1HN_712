x, y, z = map(float, input("Nhập tọa độ điểm (x, y, z): ").split())

doi_x_oxy = (x, y, -z)
doi_x_oxz = (x, -y, z)
doi_x_oyz = (-x, y, z)

print(f"Điểm đối xứng qua Oxy: {doi_x_oxy}")
print(f"Điểm đối xứng qua Oxz: {doi_x_oxz}")
print(f"Điểm đối xứng qua Oyz: {doi_x_oyz}")
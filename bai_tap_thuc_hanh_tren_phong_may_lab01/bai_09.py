#Tìm điểm đối xứng qua Oxy, Oxz, Oyz
print('Nhập tọa độ của điểm cần xét')
x=float(input('Nhập tọa độ x: '))
y=float(input('Nhập tọa độ y: '))
z=float(input('Nhập tọa độ z: '))
print(f'Tọa độ đối xứng qua Oxy là ({x},{y},{-z})')
print(f'Tọa độ đối xứng qua Oxz là ({x},{-y},{z})')
print(f'Tọa độ đối xứng qua Oyz là ({-x},{y},{z})')
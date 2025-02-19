xA = int(input("Nhập tọa độ x đỉnh A"))
yA = int(input("Nhập tọa độ y đỉnh  A "))

xB = int(input("Nhập tọa độ x đỉnh B"))
yB = int(input("Nhập toạ độ y đỉnh B "))

xC = int(input("Nhập tọa độ x đỉnh C"))
yC = int(input("Nhập toaj độ y đỉnh C"))

xG = int(((xA + xB + xC) / 3 ) *100) / 100
yG  = int(((yA + yB + yC)/3) * 100)/ 100

print("Tọa độ trong tâm G là " , xG , yG )
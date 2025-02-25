x_A = float(input("Nhập hoành độ A: "))
y_A = float(input("Nhập tung độ A: "))
x_B = float(input("Nhập hoành độ B: "))
y_B = float(input("Nhập tung độ B: "))
x_C = float(input("Nhập hoành độ C: "))
y_C = float(input("Nhập tung độ C: "))
tong_x = x_A + x_B + x_C
tong_y = y_A + y_B + y_C
x_G = tong_x / 3
y_G = tong_y / 3
print("Trọng tâm của tam giác có hoành độ: %0.2f" % x_G)
print("Trọng tâm của tam giác có tung độ: %0.2f" % y_G)
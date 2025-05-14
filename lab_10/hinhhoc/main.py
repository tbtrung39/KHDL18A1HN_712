import my_Triange
import my_square

def menu():
    print("\nCHƯƠNG TRÌNH QUẢN LÝ HÌNH HỌC")
    print("1. Tính chu vi và diện tích tam giác")
    print("2. Tính chu vi và diện tích hình vuông")
    print("0. Thoát")

while True:
    menu()
    choice = input("Chọn chức năng: ")

    if choice == "1":
        print("\n--- TAM GIÁC ---")
        a = float(input("Nhập cạnh a: "))
        b = float(input("Nhập cạnh b: "))
        c = float(input("Nhập cạnh c: "))
        if my_Triange.is_TamGiac(a, b, c):
            cv = my_Triange.ChuviTamGiac(a, b, c)
            dt = my_Triange.S_TamGiac(a, b, c)
            print("Chu vi:", cv)
            print("Diện tích: ", dt)
        else:
            print("Ba cạnh không tạo thành tam giác.")

    elif choice == "2":
        print("\n--- HÌNH VUÔNG ---")
        a = float(input("Nhập độ dài cạnh hình vuông: "))
        cv = my_square.ChuviHinhvuong(a)
        dt = my_square.Dien_tich_hinh_vuong(a)
        print("Chu vi: ", cv)
        print("Diện tích:", dt)

    elif choice == "0":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
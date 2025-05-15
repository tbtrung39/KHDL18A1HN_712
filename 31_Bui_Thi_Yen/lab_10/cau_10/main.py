from hinhhoc import (is_TamGiac, ChuviTamGiac, S_TamGiac,
                    ChuviHinhVuong, DienTichHinhVuong)

def main():
    print("CHƯƠNG TRÌNH TÍNH TOÁN HÌNH HỌC")
    print("1. Tính toán tam giác")
    print("2. Tính toán hình vuông")
    
    choice = input("Chọn loại hình (1 hoặc 2): ")
    
    if choice == '1':
        print("\nTÍNH TOÁN TAM GIÁC")
        a = float(input("Nhập cạnh a: "))
        b = float(input("Nhập cạnh b: "))
        c = float(input("Nhập cạnh c: "))
        
        if is_TamGiac(a, b, c):
            print(f"Chu vi tam giác: {ChuviTamGiac(a, b, c)}")
            print(f"Diện tích tam giác: {S_TamGiac(a, b, c):.2f}")
        else:
            print("Ba cạnh này không tạo thành tam giác")
            
    elif choice == '2':
        print("\nTÍNH TOÁN HÌNH VUÔNG")
        a = float(input("Nhập độ dài cạnh: "))
        print(f"Chu vi hình vuông: {ChuviHinhVuong(a)}")
        print(f"Diện tích hình vuông: {DienTichHinhVuong(a)}")
        
    else:
        print("Lựa chọn không hợp lệ")

if __name__ == "__main__":
    main()
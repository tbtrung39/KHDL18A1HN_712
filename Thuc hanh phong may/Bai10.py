from hinhhoc import my_Triage, my_square

def main():
    print("=== TAM GIÁC ===")
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if my_Triage.is_TamGiac(a, b, c):
        print("Là tam giác")
        print("Chu vi tam giác:", my_Triage.ChuViTamGiac(a, b, c))
        print("Diện tích tam giác:", my_Triage.S_TamGiac(a, b, c))
    else:
        print("Không phải tam giác")

    print("\n=== HÌNH VUÔNG ===")
    canh = float(input("Nhập cạnh hình vuông: "))
    print("Chu vi hình vuông:", my_square.ChuViHinhVuong(canh))
    print("Diện tích hình vuông:", my_square.Dien_tich_hinh_vuong(canh))

if __name__ == "__main__":
    main()

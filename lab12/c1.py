import math

def la_so_duong(x):
    try:
        val = float(x)
        if val <= 0:
            raise ValueError("Giá trị phải là số dương!")
        return val
    except ValueError as e:
        print(f"Lỗi: {e}")
        return None

def la_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a

def tinh_dien_tich(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def main():
    while True:
        try:
            a = la_so_duong(input("Nhập cạnh a: "))
            b = la_so_duong(input("Nhập cạnh b: "))
            c = la_so_duong(input("Nhập cạnh c: "))

            if None in (a, b, c):
                continue

            if not la_tam_giac(a, b, c):
                raise ValueError("Ba cạnh không tạo thành tam giác!")

            dientich = tinh_dien_tich(a, b, c)
            print(f"Diện tích tam giác là: {dientich:.2f}")
            break

        except ValueError as e:
            print(f"Lỗi: {e}. Vui lòng nhập lại.\n")

if __name__ == "__main__":
    main()
from equation_solver import solve_linear_equation, solve_quadratic_equation

def main():
    print("Chương trình giải phương trình")
    print("1. Giải phương trình bậc nhất: ax + b = 0")
    print("2. Giải phương trình bậc hai: ax² + bx + c = 0")
    
    choice = input("Chọn loại phương trình (1 hoặc 2): ")
    
    if choice == '1':
        a = float(input("Nhập hệ số a: "))
        b = float(input("Nhập hệ số b: "))
        result = solve_linear_equation(a, b)
        print("Kết quả:", result)
    elif choice == '2':
        a = float(input("Nhập hệ số a: "))
        b = float(input("Nhập hệ số b: "))
        c = float(input("Nhập hệ số c: "))
        result = solve_quadratic_equation(a, b, c)
        print("Kết quả:", result)
    else:
        print("Lựa chọn không hợp lệ")

if __name__ == "__main__":
    main()
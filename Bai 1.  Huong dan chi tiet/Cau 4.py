# Cau 4.

def divide_two_numbers():
    try:
        num1 = int(input("Nhap so thu nhat: "))
        num2 = int(input("Nhap so thu hai: "))
        if num2 == 0:
            raise ZeroDivisionError("So bi chia khong the bang 0")
        result = num1 / num2
    except ValueError:
        print("So nhap khong hop le, ban can phai nhap mot so nguyen")
    except ZeroDivisionError as e:
        print(e)
    else:
        print(f"{num1} chia cho {num2} bang {result}")
    finally:
        print("Chuong trinh da ket thuc")
divide_two_numbers()

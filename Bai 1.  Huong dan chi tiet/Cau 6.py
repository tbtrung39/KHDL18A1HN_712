# Cau 6.

def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b
try:
    num1 = int(input("Nhap so tu so: "))
    num2 = int(input("Nhap so mau so: "))
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")
except AssertionError as e:
    print("Loi:", e)
except ValueError:
    print("Ban phai nhap so nguyen")
except:
    print("Da co loi xay ra")

def is_triangle(a,b,c):
    return a+b>c and a+c>b and b+c>a 
try:
    a=float(input("Nhập cạnh a: "))
    b=float(input("Nhập cạnh b: "))
    c=float(input("Nhập cạnh c: "))
    if a<=0 or b<=0 or c<=0:
        raise ValueError("Cạnh tam giác phải là số dương lớn hơn 0.")
    if not is_triangle(a,b,b):
        raise ValueError("Ba cạnh không thỏa mãn điều kiện tạo thành tam giác")
    print(f"Ba cạnh ({a},{b},{c}) tạo thành một tam giác hợp lệ")
except ValueError as ve:
    print("loi:",ve)
except Exception as e:
    print("Đã xảy ra lỗi không xác định:",e)
try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    
    # Kiểm tra điều kiện là 3 cạnh tam giác
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Cạnh phải lớn hơn 0.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Ba cạnh không tạo thành tam giác.")
    
    print("Ba cạnh hợp lệ của một tam giác.")
except ValueError as e:
    print("Lỗi:", e)
except:
    print("Lỗi: Dữ liệu không hợp lệ.")

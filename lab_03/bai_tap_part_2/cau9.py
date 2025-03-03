#BAI11A
h = int(input("Nhập số hàng của tam giác: "))  

# Vòng lặp bên ngoài xác định số dòng
for dong in range(1, h + 1):  
    # Vòng lặp bên trong xử lý số lượng ký tự '*'
    for cot in range(1, dong + 1):  
        print("*", end=" ")  
    # Kết thúc mỗi dòng
    print("\r")


#BAI11C
h = int(input("Nhập số hàng của tam giác: "))  
k = h - 1  # Xác định số khoảng trắng  
# Vòng lặp bên ngoài xác định số dòng
for dong in range(1, h + 1):  
    # In khoảng trắng trước dấu *
    for space in range(1, k + 1):  
        print(" ", end=" ")  
    # Giảm k đi 1 sau mỗi dòng
    k -= 1  
    # In dấu *
    if dong == 1 or dong == h:  
        for cot in range(1, dong + 1):  
            print("*", end=" ")  
    else:  
        print("*", end=" ")  
        for cot in range(1, dong - 1):  
            print(" ", end=" ")  
        print("*", end=" ")  
    # Kết thúc mỗi dòng
    print("\r")

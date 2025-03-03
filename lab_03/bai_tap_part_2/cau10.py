#BAI11B
h = int(input("Nhập số hàng của tam giác: "))  

# Vòng lặp bên ngoài xác định số dòng
for dong in range(1, h + 1):  
    # Xử lý viền ngoài và viền dưới
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
 

#7.a
h=int(input("Nhập chiều cao tam giác: ")) 
#Vòng lặp bên ngoài xác định số dòng, trong bài này là h 
for i in range(0,h): 
    #Vòng lặp bên trong giữ số cột có 
    #các giá trị thay đổi đối với vòng lặp ngoài 
    for j in range(0,i+1): 
        #in các trạng thái 
        print("* ",end='') 
 
    #Kết thúc sau mỗi dòng  
    print("\r")     #'\r' xuống dòng và đưa con trỏ về đầu dòng 

#7.b
h=int(input("Nhập giá trị chiều cao tam giác: ")) 
# Xác định số khoảng trắng 
k = 2*h -2 
# Vòng lặp bên ngoài xác định số dòng  
for dong in range(1, h+1):  
    # Vòng lặp trong để xác định số khoảng trắng  
    # thay đổi các giá trị tùy yêu cầu 
    for cot in range(1, k+1):  
        #in số dấu cách 
        print(end=" ")  
    #vòng lặp bên trong để xử lý số lượng giá trị cột  
    #thay đổi theo vòng lặp bên ngoài 
    for cot in range(1, dong+1):        
        # in  
        print("*", end=" ")  
    #Giảm k sau mỗi lầm kết thúc dòng 
    k=k-2   
    # ending line after each row  
    print("\r") 

#7.d
h=int(input('Nhập chiều cao tam giác số :')) 
num = 1 
for dong in range(1, h+1):     
    num = 1  
    for cot in range(1, dong+1):         
        print(num, end=" ") 
        num = num + 1  
    print("\r") 

#7.e
h=int(input("Nhập giá trị chiều cao tam giác cân: "))  
k = 2*h -2   
for dong in range(1, h+1):  
    for cot in range(1, k+1): 
        print(end=" ") 
    for cot in range(1, dong+1):        
        print("*", end=" ")  
    k=k-1 
    print("\r") 

#7.f
num = 65 
h=int(input('Nhập chiều cao tam giác ký tự: ') )  
for i in range(0, h):  
        for j in range(0, i+1):   
            ch = chr(num)
            print(ch, end=" ")    
        num = num + 1 
        print("\r")  
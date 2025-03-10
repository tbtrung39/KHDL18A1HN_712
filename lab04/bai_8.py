c = input("Nhập một ký tự: ")  
i = 0  
while i < 256:
    if chr(i) == c:
        print("Mã ASCII của ký tự", c, "là:", i)  
        break  
    i += 1
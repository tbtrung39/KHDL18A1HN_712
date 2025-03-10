num = int(input("Nhập một số: "))  
result = ""  
num_str = str(num)  
i = 0  
while i < len(num_str):  
    if num_str[i] == "0": result += "không "  
    elif num_str[i] == "1": result += "một "  
    elif num_str[i] == "2": result += "hai "  
    elif num_str[i] == "3": result += "ba "  
    elif num_str[i] == "4": result += "bốn "  
    elif num_str[i] == "5": result += "năm "  
    elif num_str[i] == "6": result += "sáu "  
    elif num_str[i] == "7": result += "bảy "  
    elif num_str[i] == "8": result += "tám "  
    elif num_str[i] == "9": result += "chín "  
    i += 1  
print("Kết quả:", result)
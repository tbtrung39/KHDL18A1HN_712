a = input("Nhập chuỗi ký tự : ") 
b = str()
S = 0 
for i  in a : 
    if "0" <= i <= "9" : 
        b += i 
b = int(b)
for i in range(1,b) : 
    if b % i == 0 : 
        S += i 
if S == b : 
    print(f"{b} là số hoàn hảo ")
else : 
    print(f"{b} không phải số hoàn hảo ")
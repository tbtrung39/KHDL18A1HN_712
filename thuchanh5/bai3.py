n = int(input("Nhập hệ cơ số 10 ")) 
hcs2 = str()
check = n 
while True : 
    hcs2 = str(check % 2) + hcs2 
    if check // 2 == 0 : 
        break 
    check  = check //2 
print(f"hệ cơ số 2 của {n} là {hcs2}")
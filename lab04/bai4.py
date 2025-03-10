tuso = int(input("Nhập tử số : "))
mauso = int(input("Nhập mẫu số : "))
if mauso == 0 : 
    print("Mẫu số không hợp lệ vui lòng nhập lại ")
else : 
    ucln = 1
    rutgon = 0 
    while ucln <= tuso or ucln <= mauso : 
        if tuso % ucln == 0 and mauso % ucln == 0 : 
            rutgon = ucln 
        ucln += 1 

    tsorg = tuso / rutgon 
    msorg = mauso / rutgon  
    print(f"PHân số sau khi rút gọn là {int(tsorg)}/{int(msorg)} ")
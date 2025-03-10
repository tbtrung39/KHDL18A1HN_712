so1 = int(input("Nhập số thứ nhất : "))
so2 = int(input("NHập số thứ hai : ")) 
bcnn = 1 
check = 0 
while True : 
    if bcnn % so1==0  and bcnn %so2 == 0 : 
        check = bcnn 
        break 
    bcnn += 1 
print("Bội chung nhỏ nhất của hai số là ",check )
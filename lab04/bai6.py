n = int(input("Nhập số bất kì : "))
s = str(n) 
i = 0
ketqua = str()
while i < len(s): 
    if int(s[i]) == 0:
        ketqua += "Không "
    elif int(s[i]) == 1:
        ketqua += "Một "
    elif int(s[i]) == 2:
        ketqua += "Hai "
    elif int(s[i]) == 3:
        ketqua += "Ba "
    elif int(s[i]) == 4:
        ketqua += "Bốn "
    elif int(s[i]) == 5:
        ketqua += "Năm "
    elif int(s[i]) == 6:
        ketqua += "Sáu "
    elif int(s[i]) == 7:
        ketqua += "Bảy "
    elif int(s[i]) == 8:
        ketqua += "Tám "
    elif int(s[i]) == 9:
        ketqua += "Chín "
    i += 1 
print(ketqua)

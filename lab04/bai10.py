n = input("Nhập số thập phân bất kì ")
s = str(n) 
i = 0
ketqua = str()
while i < len(s): 
    if s[i] == "0":
        ketqua += "Không "
    elif (s[i]) == "1":
        ketqua += "Một "
    elif (s[i]) == "2":
        ketqua += "Hai "
    elif (s[i]) == "3":
        ketqua += "Ba "
    elif (s[i]) == "4":
        ketqua += "Bốn "
    elif (s[i]) == "5":
        ketqua += "Năm "
    elif (s[i]) == "6":
        ketqua += "Sáu "
    elif (s[i]) == "7":
        ketqua += "Bảy "
    elif (s[i]) == "8":
        ketqua += "Tám "
    elif (s[i]) == "9":
        ketqua += "Chín "
    elif s[i] == "." : 
        ketqua += " chấm"
    i += 1 
print(ketqua)

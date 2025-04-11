s1 = input("Nhập chuỗi thứ nhất : ")
s2 = input("Nhập chuỗi thứ hai : ")
max_len = 0
chuoi_chung = ""
for i in range(len(s1)):
    for j in range(len(s2)):
        dem = 0
        while (i + dem < len(s1)) and (j +dem < len(s2)) and (s1[i + dem] ==s2[j + dem]):
            dem+=1
            if dem > max_len:
                max_len = dem
                chuoi_chung = s1[i:i+dem]
if max_len > 0 :
    print("Chuỗi con chung dài nhất là : ",chuoi_chung)
else:
    print("Không có chuỗi con chung.")
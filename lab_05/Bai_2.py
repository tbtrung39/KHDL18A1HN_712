s=input("Nhap chuoi: ")
c=0
for x in s:
    if not ( "A" <=x <= "Z" or "a"<=x<='z' or  "0"<=x<="9") :
        c+=1
print("So ky tu khong phai chu cai tieng anh va khong phai la so:",c)

def chuoi_ky_tu():
    try:
        str = input("Nhap chuoi ky tu: ")
        if not str.isalpha():
            raise Exception ("Loi ky tu!!")
        for i in range(len(str)-1):
            if str[i] == str[i+1]:
                raise Exception ("Loi nhap lieu!!!")
        for i in range(len(str)-3):
            if str[i:i+4] in str[i+1:]:
                raise Exception ("loi nhap trung nhau") 
        print("Chuoi hop le")
    except Exception as a:
        print("Loi",a) 
chuoi_ky_tu()    
while True:
    try:
        s = input("Nhap chuoi: ")
        if not s.isalpha():
            raise ValueError("loi ki tu")
        if any(s[i] == s[i +1] for i in range(len(s)-1)): raise ValueError("loi nhap")
        if any(len(set(s[i:i+5])) == 1 for i in range(len(s) - 4)): raise ValueError("loi nhap,nhap lai")
        print("chuoi hop le",s)
        break
    except ValueError as e:
        print(e)
        
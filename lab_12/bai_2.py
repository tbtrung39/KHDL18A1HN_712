def kiem_tra(s):
    for c in s:
        if not (c.isalpha() or c.isspace()):
            raise Exception("Loi ky tu")
    for i in range(len(s) - 1):
        if s[i] == s[i+1] and s[i] != ' ':
            raise Exception("Loi nhap lieu")
    for i in range(len(s) - 3):
        if s[i] == s[i+1] == s[i+2] == s[i+3] and s[i] != ' ':
            raise Exception("Loi nhap lap lai")
    tu = s.split()
    for i in range(len(tu) - 4):
        if tu[i] == tu[i+1] == tu[i+2] == tu[i+3] == tu[i+4]:
            raise Exception("Loi nhap trung lap")

while True:
    try:
        s = input("Nhap chuoi: ")
        kiem_tra(s)
        print("Chuoi hop le.")
        break
    except Exception as e:
        print("Loi:", e)
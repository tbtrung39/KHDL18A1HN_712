# Cau 3. 

def chay_bai_3():
    try:
        with open("Bai 2. Thuc hanh phong may/dulieu.txt", 'r', encoding='utf-8') as f:
            noi_dung = f.read()
        with open("Bai 2. Thuc hanh phong may/copy.dat", 'w', encoding='utf-8') as f_copy:
            f_copy.write(noi_dung)
        
        print("Noi dung da duoc copy sang tap tin copy.dat")
        
    except FileNotFoundError:
        print("Tap tin khong ton tai. Ket thuc chuong trinh.")
    except Exception as e:
        print("Da xay ra loi:", e)
chay_bai_3()
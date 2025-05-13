# Cau 4.

def chay_bai_4():
    try:
        ten_nguon = input("Nhap ten tap tin nguon (de doc): ")
        ten_dich = input("Nhap ten tap tin dich (de ghi): ")
        try:
            with open(ten_nguon, 'r', encoding='utf-8') as f_in:
                noi_dung = f_in.read()
        except FileNotFoundError:
            print("Khong tim thay tap tin nguon.")
            return
        except IOError:
            print("Loi khi doc tap tin nguon.")
            return
        try:
            with open(ten_dich, 'w', encoding='utf-8') as f_out:
                f_out.write(noi_dung)
        except IOError:
            print("Loi khi ghi vao tap tin dich.")
            return
        print("Da sao chep noi dung thanh cong vao tap tin moi.")
    except Exception as e:
        print("Da xay ra loi:", e)
chay_bai_4()

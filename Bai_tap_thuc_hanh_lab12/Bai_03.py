def sao_chep_tap_tin():
    try:
        ten_file = input("Nhap ten tap tin can doc(hoac paste duong dan vao): ")
        with open(ten_file, 'r', encoding="utf-8") as f:
            noi_dung = f.read()
        with open("copy.dat", "w", encoding="utf-8") as f_copy:
            f_copy.write(noi_dung)
        print("Da sao chep")
    except FileNotFoundError:
        print(f"Tap tin {ten_file} ko ton tai")
    except Exception as e:
        print("Da xay ra loi: {e}")
sao_chep_tap_tin()
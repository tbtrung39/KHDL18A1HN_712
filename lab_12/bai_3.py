try:
    ten = input("Nhap ten file can doc: ")

    with open(ten, "r", encoding="utf-8") as f:
        nd = f.read()

    with open("copy.dat", "w", encoding="utf-8") as f2:
        f2.write(nd)

    print("Da sao chep noi dung vao 'copy.dat'.")

except FileNotFoundError:
    print("Loi: Khong tim thay file ban da nhap.")
except Exception as e:
    print("Loi khac:", e)
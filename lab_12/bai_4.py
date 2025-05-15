try:
    ten_nguon = input("Nhap ten file nguon: ")
    ten_dich = input("Nhap ten file dich: ")

    f1 = open(ten_nguon, "r", encoding="utf-8")
    f2 = open(ten_dich, "w", encoding="utf-8")

    for dong in f1:
        f2.write(dong)

    print(f"Da sao chep noi dung tu '{ten_nguon}' sang '{ten_dich}'.")

    f1.close()
    f2.close()

except FileNotFoundError:
    print("Loi: Khong tim thay file nguon.")

except IOError:
    print("Loi khi thao tac file (co the do sai che do mo).")

except Exception as e:
    print("Loi khac:", e)

finally:
    try:
        f1.close()
    except:
        pass
    try:
        f2.close()
    except:
        pass
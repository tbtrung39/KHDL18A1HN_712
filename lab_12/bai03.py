try:
    tên_tập_tin = input("Nhập tên tập tin: ")
    mở = open(tên_tập_tin, "r", encoding="utf-8")
    nội_dung = mở.read()
    mở.close()

    print("Nội dung tập tin:")
    print(nội_dung)

    tên_mới = "copy.txt"
    ghi = open(tên_mới, "w", encoding="utf-8")
    ghi.write(nội_dung)
    ghi.close()

    print("Nội dung đã được sao chép vào", tên_mới)
except FileNotFoundError:
    print("Tập tin không tồn tại.")
try:
    tên_tập_tin = input("Nhập tên tập tin cần ghi: ")
    nội_dung = input("Nhập nội dung cần ghi vào tập tin: ")

    với_ghi = open(tên_tập_tin, "w", encoding="utf-8")
    với_ghi.write(nội_dung)
    với_ghi.close()

    print("Đã ghi nội dung vào tập tin", tên_tập_tin)
except Exception as lỗi:
    print("Lỗi:", lỗi)
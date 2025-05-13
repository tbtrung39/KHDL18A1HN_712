try:
    ten_tap_tin_doc=input("Nhập tên tập tin cần đọc:")
    ten_tap_tin_ghi=input("Nhập tên tập tin để ghi nội dung: ")
    with open(ten_tap_tin_doc,'r',encoding='utf-8') as f_doc:
        noi_dung=f_doc.read()
    try:
        with open(ten_tap_tin_ghi,'w',encoding='utf-8') as f_ghi:
            f_ghi.write(noi_dung)
        print("đã ghi nội dung thành công vào tập tin mới")
    except IOError:
        print("lỗi. không thể mở tập tin để ghi. hãy kiểm tra chế độ mở hoặc quyền truy cập")
except FileNotFoundError:
    print("lỗi. tập tin đọc không tồn tại")
except Exception as e:
    print("đã xảy ra lỗi:",e)
finally:
    print("chương trình kết thúc và đã đóng tất cả tập tin")
try:
    ten_tap_tin=input("Nhập tên tập tin cần đọc:")
    with open(ten_tap_tin,'r',encoding='utf-8') as f:
        noi_dung=f.read()
    with open('copy.dat','w',encoding='utf-8') as f_copy:
        f_copy.write(noi_dung)
    print("đã sao chép nội dung sang tập tin copy.dat")
except FileNotFoundError:
    print("lỗi: không tìm thấy tệp tin")
except Exception as e:
    print("đã xảy ra lỗi:",e)

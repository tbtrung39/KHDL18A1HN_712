try:
    
    ten_nguon = input("Nhập tên tập tin nguồn (hoặc paste đường dẫn vào ):    ")
    ten_dich = input("Nhập tên tập tin cần chuyển đén (hoặc paste đường dẫn vào):    ")
    with    open(ten_nguon, 'r', encoding='utf-8')    as    f:
      noi_dung    =    f.read()
    with    open(ten_dich, 'w', encoding='utf-8')    as    f2:
      f2.write(noi_dung)
    print('đã sao chép từ [{ten_nguon}    sang    {ten_dich}]')
except    FileNotFoundError:
    print(f"tập tin tên[{ten_nguon}]    khong    tồn    tại")
except    Exception    as    e:
    print('đẫ lỗi', e)

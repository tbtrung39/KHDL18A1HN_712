try:
    
    ten_nguon    =    input("Nhap    ten    tap    tin    nguon:    ")
    ten_dich    =    input("Nhap    ten    tap    tin    dich:    ")
    with    open(ten_nguon,    'r',    encoding='utf-8')    as    f:
      noi_dung    =    f.read()
    with    open(ten_dich,    'w',    encoding='utf-8')    as    f2:
      f2.write(noi_dung)
    print('da    sao    chep    noi    dungtu[{ten_nguon}    sang    {ten_dich}]')
except    FileNotFoundError:
    print(f"tap    tinnguon[{ten_nguon}]    khong    ton    tai")
except    Exception    as    e:
    print('dax loi', e)

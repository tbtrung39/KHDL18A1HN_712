def xu_ly_checkin(fileM, fileN):
    with open(fileM, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])  
    passengers = lines[1:]

    tong_trong_luong = []
    canceled = []

    for idx, line in enumerate(passengers, start=1):
        weights = list(map(float, line.split()))
        total_weight = sum(weights)
        count_items = len(weights)
        tong_trong_luong.append(total_weight)

        if total_weight > 23:
            canceled.append((idx, 'vượt quá 23kg'))
        elif count_items > 5:
            canceled.append((idx, 'quá 5 kiện'))

    with open(fileN, 'w') as f_out:
        for w in tong_trong_luong:
            f_out.write(f"{w:.2f}\n")

    with open('CANCELED.OUT', 'w') as f_can:
        for item in canceled:
            f_can.write(f"{item[0]}\n")
    if canceled:
        print("DANH SÁCH HÀNH KHÁCH BỊ HỦY CHUYẾN:")
        for idx, ly_do in canceled:
            print(f"Hành khách {idx} bị hủy chuyến do {ly_do}.")
    else:
        print("Không có hành khách nào bị hủy chuyến.")

fileM = input('Nhập đường dẫn đến file PASSENGERS.IN: ')
fileN = input('Nhập đường dẫn đến file WEIGHT.OUT: ')

xu_ly_checkin(fileM, fileN)
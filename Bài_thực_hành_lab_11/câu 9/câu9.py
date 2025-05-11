def xu_ly_checkin(fileM, fileN):
    with open(fileM, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    n = int(lines[0])  # số hành khách
    passengers = lines[1:]

    tong_trong_luong = []
    canceled = []

    for idx, line in enumerate(passengers, start=1):
        # Chuyển từng dòng thành danh sách số thực
        weights = list(map(float, line.split()))
        total_weight = sum(weights)
        count_items = len(weights)
        tong_trong_luong.append(total_weight)

        # Kiểm tra điều kiện bị hủy
        if total_weight > 23:
            canceled.append((idx, 'vượt quá 23kg'))
        elif count_items > 5:
            canceled.append((idx, 'quá 5 kiện'))

    # Ghi file WEIGHT.OUT
    with open(fileN, 'w') as f_out:
        for w in tong_trong_luong:
            f_out.write(f"{w:.2f}\n")

    # Ghi file CANCELED.OUT
    with open('CANCELED.OUT', 'w') as f_can:
        for item in canceled:
            f_can.write(f"{item[0]}\n")

    # In ra màn hình thông báo
    if canceled:
        print("DANH SÁCH HÀNH KHÁCH BỊ HỦY CHUYẾN:")
        for idx, ly_do in canceled:
            print(f"Hành khách {idx} bị hủy chuyến do {ly_do}.")
    else:
        print("Không có hành khách nào bị hủy chuyến.")

# Gọi hàm chính
fileM = input('Nhập đường dẫn đến file PASSENGERS.IN: ')
fileN = input('Nhập đường dẫn đến file WEIGHT.OUT: ')

xu_ly_checkin(fileM, fileN)

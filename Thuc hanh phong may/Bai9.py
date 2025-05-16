# Tạo file PASSENGER.IN mẫu như ví dụ
def tao_file_passenger():
    with open('PASSENGER.IN', 'w') as f:
        f.write('5\n')
        f.write('20.5\n')
        f.write('1.3 1.5 3.5 2.3\n')
        f.write('7.25 3.5 7\n')
        f.write('11 7.45 10.8 5.6\n')
        f.write('4 6 8\n')

# Đọc dữ liệu từ file PASSENGER.IN
def doc_du_lieu(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    so_khach = int(lines[0].strip())
    hanh_ly = [list(map(float, line.strip().split())) for line in lines[1:]]
    return so_khach, hanh_ly

# Ghi tổng trọng lượng hành lý xách tay vào WEIGHT.OUT
def ghi_weight_out(tong_weights):
    with open('WEIGHT.OUT', 'w') as f:
        for w in tong_weights:
            f.write(f"{w:.2f}\n")

# Ghi danh sách hành khách bị hủy chuyến vào CANCELED.OUT
def ghi_canceled_out(canceled):
    with open('CANCELED.OUT', 'w') as f:
        for idx, ly_do in canceled:
            f.write(f"{idx} -> {ly_do}\n")

# Xử lý điều kiện hủy chuyến
def xu_ly_hanh_ly(so_khach, hanh_ly):
    tong_weights = []
    canceled = []

    for i in range(so_khach):
        tong = sum(hanh_ly[i])
        so_mon = len(hanh_ly[i])
        tong_weights.append(tong)

        if tong > 23:
            canceled.append((i + 1, "tổng trọng lượng > 23 kg"))
        elif so_mon > 5:
            canceled.append((i + 1, "số lượng hành lý > 5"))

    return tong_weights, canceled

# In thông báo ra màn hình
def in_thong_bao(canceled):
    if not canceled:
        print("Không có hành khách nào bị hủy chuyến.")
    else:
        print("Danh sách hành khách bị hủy chuyến:")
        for idx, ly_do in canceled:
            print(f"- Hành khách thứ {idx}: {ly_do}")
def main():
    tao_file_passenger()
    so_khach, hanh_ly = doc_du_lieu('PASSENGER.IN')
    tong_weights, canceled = xu_ly_hanh_ly(so_khach, hanh_ly)
    ghi_weight_out(tong_weights)
    ghi_canceled_out(canceled)
    in_thong_bao(canceled)

if __name__ == "__main__":
    main()

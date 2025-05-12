def doc_du_lieu(file_path):
    with open(file_path, 'r') as f:
        gioi_han = float(f.readline())
        hanh_ly = [list(map(float, line.split())) for line in f]
    return gioi_han, hanh_ly

def tinh_tong_trong_luong(ds_hanh_ly):
    return [sum(hanh_ly) for hanh_ly in ds_hanh_ly]

def ghi_file_weight(tong_trong_luong, file_path):
    with open(file_path, 'w') as f:
        for tong in tong_trong_luong:
            f.write(f"{tong:.2f}\n")

def ghi_file_canceled(tong_trong_luong, gioi_han, file_path):
    with open(file_path, 'w') as f:
        for i, tong in enumerate(tong_trong_luong, start=1):
            if tong > 23 or tong > gioi_han:
                f.write(f"{i} -> Số thứ tự của khách có tổng trọng lượng vượt quá\n")

def main():
    gioi_han, ds_hanh_ly = doc_du_lieu(r"bai9\PASSENGER.IN")
    tong_trong_luong = tinh_tong_trong_luong(ds_hanh_ly)

    ghi_file_weight(tong_trong_luong, r"bai9\WEIGHT.OUT")
    ghi_file_canceled(tong_trong_luong, gioi_han, r"bai9\CANCELED.OUT")

    print("Đã xử lý xong. Kết quả lưu vào WEIGHT.OUT và CANCELED.OUT")

if __name__ == "__main__":
    main()

def tao_set_ky_tu():
    """Khởi tạo một set các ký tự nhập từ bàn phím cho đến khi bấm ESC."""
    ky_tu_set = set()
    print("Nhập các ký tự (nhấn ESC để kết thúc):")
    while True:
        ky_tu = input()
        if ky_tu == '\x1b':  # Mã ASCII của phím ESC
            break
        if len(ky_tu) == 1:
            ky_tu_set.add(ky_tu)
        else:
            print("Vui lòng chỉ nhập một ký tự.")
    return ky_tu_set

def xoa_ky_tu_so(input_set):
    """Xóa các ký tự số khỏi tập hợp."""
    ky_tu_set_moi = set()
    for ky_tu in input_set:
        if not '0' <= ky_tu <= '9':
            ky_tu_set_moi.add(ky_tu)
    return ky_tu_set_moi

if __name__ == "__main__":
    tap_hop_ky_tu = tao_set_ky_tu()
    print("\nTập hợp các ký tự đã nhập:", tap_hop_ky_tu)
    tap_hop_sau_xoa = xoa_ky_tu_so(tap_hop_ky_tu)
    print("Tập hợp sau khi xóa các ký tự số:", tap_hop_sau_xoa)
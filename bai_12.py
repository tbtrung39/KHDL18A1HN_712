def giai_bai_toan_ga_cho_de_quy(tong_con, tong_chan, so_ga=0):
    """Giải bài toán gà và chó bằng đệ quy."""
    if so_ga > tong_con:
        return None

    so_cho = tong_con - so_ga
    tong_chan_tinh = so_ga * 2 + so_cho * 4

    if tong_chan_tinh == tong_chan:
        return so_ga, so_cho
    elif so_ga < tong_con:
        result = giai_bai_toan_ga_cho_de_quy(tong_con, tong_chan, so_ga + 1)
        return result
    else:
        return None

if __name__ == "__main__":
    tong_con = 36
    tong_chan = 100
    ket_qua = giai_bai_toan_ga_cho_de_quy(tong_con, tong_chan)

    if ket_qua:
        so_ga, so_cho = ket_qua
        print(f"Có {ket_qua[0]} con gà và {ket_qua[1]} con chó.")
    else:
        print("Không tìm thấy nghiệm hợp lệ.")
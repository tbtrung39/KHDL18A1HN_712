def giai_toan(so_ga, so_cho):
    if so_ga + so_cho == 36 and (so_ga * 2 + so_cho * 4) == 100:
        return so_ga, so_cho
    if so_ga > 36 or so_cho < 0:
        return None
    return giai_toan(so_ga + 1, so_cho - 1)

def tim_so_con_vat():
    ket_qua = giai_toan(0, 36)
    if ket_qua:
        print(f"Số con gà: {ket_qua[0]}, Số con chó: {ket_qua[1]}")
    else:
        print("Không tìm được lời giải.")

tim_so_con_vat()

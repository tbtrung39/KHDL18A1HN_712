#a
def nhap_ma_tran():
    """Nhập vào một ma trận từ bàn phím."""
    m = int(input("Nhập số hàng của ma trận: "))
    n = int(input("Nhập số cột của ma trận: "))
    A = []
    print("Nhập các phần tử của ma trận:")
    for i in range(m):
        hang = []
        for j in range(n):
            while True:
                try:
                    phan_tu = int(input(f"Nhập phần tử A[{i+1}][{j+1}]: "))
                    if phan_tu >= 0:
                        hang.append(phan_tu)
                        break
                    else:
                        print("Vui lòng nhập số tự nhiên (lớn hơn hoặc bằng 0).")
                except ValueError:
                    print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")
        A.append(hang)
    return A
#b
def tinh_tong_ma_tran(A):
    """Tính tổng các phần tử của ma trận."""
    tong = 0
    for hang in A:
        tong += sum(hang)
    return tong

if __name__ == "__main__":
    ma_tran = nhap_ma_tran()
    print("\nMa trận bạn vừa nhập là:")
    for hang in ma_tran:
        print(hang)

    tong_cac_phan_tu = tinh_tong_ma_tran(ma_tran)
    print("\nTổng các phần tử của ma trận là:", tong_cac_phan_tu)

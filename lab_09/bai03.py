def luy_thua(a, n):
    """Hàm đệ quy tính a^n"""
    if n == 0:
        return 1
    return a * luy_thua(a, n - 1)

def main():
    a = float(input("Nhập cơ số a: "))
    n = int(input("Nhập số mũ n (>= 0): "))

    if n < 0:
        print("Chương trình hiện chỉ hỗ trợ số mũ không âm.")
        return

    ket_qua = luy_thua(a, n)
    print(f"{a}^{n} = {ket_qua}")

if __name__ == "__main__":
    main()

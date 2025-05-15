def nhap_numbers_va_tao_set():
    numbers = []
    print("Nhập các số tự nhiên (nhập 'x' để kết thúc):")
    while True:
        s = input("Nhập số: ")
        if s.lower() == 'x':
            break
        if s.isdigit():
            numbers.append(int(s))
        else:
            print("Vui lòng nhập số tự nhiên hoặc 'x' để thoát.")
    A = set(numbers)
    print("Danh sách Numbers:", numbers)
    print("Tập hợp A (các phần tử duy nhất):", A)
nhap_numbers_va_tao_set()

import msvcrt
def nhap_set_ky_tu():
    tap_ky_tu = set()
    print("Nhập các ký tự (bấm ESC để kết thúc):")
    while True:
        key = msvcrt.getch()
        if key == b'\x1b':
            break
        char = key.decode('utf-8')
        print(char, end=' ')
        tap_ky_tu.add(char)
    tap_ky_tu = {c for c in tap_ky_tu if not c.isdigit()} 
    print("\nTập hợp sau khi xoá các ký tự số:", tap_ky_tu)
nhap_set_ky_tu()

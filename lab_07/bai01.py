khoi_tao = set()
print("Nhập ký tự (bấm ESC để kết thúc):")
while True:
    char = input()
    if char == 'ESC':
        break
    if not char.isdigit(): 
        khoi_tao.add(char)
print("Tập hợp các ký tự:", khoi_tao)
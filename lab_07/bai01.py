s = set()
print("Nhập ký tự (Nhập ESC để kết thúc):")
while True:
    char = input()
    if char == 'ESC':
        break
    if not char.isdigit(): 
        s.add(char)
print("Tập hợp các ký tự:", s)
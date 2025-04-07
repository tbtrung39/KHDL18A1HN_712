char_set = set()
print("Nhập ký tự (bấm ESC để kết thúc):")
while True:
    char = input()
    if char == 'ESC':
        break
    if not char.isdigit(): 
        char_set.add(char)
print("Tập hợp các ký tự:", char_set)
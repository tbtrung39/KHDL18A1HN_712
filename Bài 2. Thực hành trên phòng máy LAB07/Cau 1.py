# Cau 1.

import msvcrt  
def get_input_set():
    char_set = set()
    print("Nhập các ký tự (bấm ESC để kết thúc):")
    while True:
        key = msvcrt.getwch()   
        if key == '\x1b':  
            break        
        char_set.add(key)   
    char_set = {char for char in char_set if not char.isdigit()}   
    return char_set
char_set = get_input_set()
print("Tập hợp sau khi loại bỏ số:", char_set)

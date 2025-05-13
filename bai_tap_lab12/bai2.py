while True:
    try:
        s = input("Nhập chuỗi: ")
        if not s.isalpha(): raise ValueError("Lỗi ký tự !!!")
        if any(s[i] == s[i+1] for i in range(len(s)-1)): raise ValueError("Lỗi nhập liệu !!!")
        if any(len(set(s[i:i+5])) == 1 for i in range(len(s)-4)): raise ValueError("Lỗi nhập lặp lại !!!")
        print("Chuỗi hợp lệ:", s); break
    except ValueError as e:
        print(e)

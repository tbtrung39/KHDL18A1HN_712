while True:
    char = input("Nhập một ký tự: ").strip()
    if len(char) == 1:
        print(f"Mã ASCII của '{char}' là: {ord(char)}")
        break 
    else:
        print("Vui lòng nhập một ký tự duy nhất!")
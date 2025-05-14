count_same = 1
prev_char = ''
repeat_chars = []

while True:
    try:
        s = input("Nhập một ký tự (hoặc 0 để thoát): ").strip()
        if len(s) != 1 or not s.isalpha():
            raise Exception("Lỗi ký tự !!!")

        if s == prev_char:
            count_same += 1
            if count_same == 2:
                raise Exception("Lỗi nhập lặp !!!")
            elif count_same == 5:
                raise Exception("Lỗi nhập trùng lặp!!!")
        else:
            count_same = 1  # reset nếu ký tự khác nhau

        prev_char = s

    except Exception as e:
        print(e)
    else:
        print("Ký tự hợp lệ:", s)

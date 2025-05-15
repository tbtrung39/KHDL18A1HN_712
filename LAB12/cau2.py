import re

def check_input(string):
    if not re.match("^[a-zA-Z]+$", string):  # Kiểm tra xem có phải ký tự chữ cái không
        raise Exception("Lỗi ký tự !!!")
    
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:  # Kiểm tra 2 ký tự liên tiếp giống nhau
            raise Exception("Lỗi nhập liệu !!!")
    
    for i in range(len(string) - 3):
        if string[i] == string[i + 1] == string[i + 2] == string[i + 3]:  # Kiểm tra 4 ký tự giống nhau liên tiếp
            raise Exception("Lỗi nhập lặp lại !!!")
    
    words = string.split()
    for i in range(len(words) - 4):
        if words[i] == words[i + 1] == words[i + 2] == words[i + 3] == words[i + 4]:  # Kiểm tra 5 từ giống nhau
            raise Exception("Lỗi nhập trùng lặp!!!")

while True:
    try:
        user_input = input("Nhập chuỗi ký tự: ")
        check_input(user_input)
        print("Chuỗi hợp lệ.")
        break
    except Exception as e:
        print(f"Lỗi: {e}")

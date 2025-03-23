str_input = input("Nhập chuỗi ký tự: ")
words = str_input.replace(",", " ").split()
print("Các từ trong chuỗi là:")
for word in words:
    print(word)

char = input("Nhập một ký tự bất kỳ: ")
while len(char) != 1:
    char = input("Vui lòng chỉ nhập một ký tự: ")
print(f"Giá trị ASCII của '{char}' là: {ord(char)}")
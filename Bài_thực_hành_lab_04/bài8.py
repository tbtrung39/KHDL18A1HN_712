# Nhập một ký tự
char = input("Nhập một ký tự bất kỳ: ")

# Kiểm tra nhập đúng 1 ký tự
while len(char) != 1:
    char = input("Vui lòng chỉ nhập một ký tự: ")

# Hiển thị giá trị ASCII
print(f"Giá trị ASCII của '{char}' là: {ord(char)}")

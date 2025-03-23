str_input = input("Nhập đoạn văn bản: ") + " "  # Thêm dấu cách để xử lý từ cuối cùng
word = input("Nhập từ đơn cần tìm: ")
count = 0
temp = ""

for char in str_input:
    if char != " ":
        temp += char
    else:
        if temp == word:
            count += 1
        temp = ""

print(f"Số lần xuất hiện của từ '{word}':", count)

Str = input("Nhập đoạn văn bản: ")
words = Str.split()
count = 0
for word in words:
    if word.isalpha():
        count += 1
print("Số từ đơn trong đoạn văn:", count)
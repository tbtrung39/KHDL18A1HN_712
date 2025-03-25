str_input = input("Nhập đoạn văn bản: ")
word = input("Nhập từ đơn cần tìm: ")
words = str_input.split()

count = words.count(word)
print(f"Số lần xuất hiện của từ '{word}':", count)
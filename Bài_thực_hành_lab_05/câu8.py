Str = input("Nhập đoạn văn bản:\n")
word = input("Nhập từ đơn cần tìm: ").strip()
words = Str.split()
count = sum(1 for w in words if w == word)
count +=1
print(f"Từ '{word}' xuất hiện {count} lần trong đoạn văn bản.")

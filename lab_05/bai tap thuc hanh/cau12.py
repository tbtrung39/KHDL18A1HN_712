Str = input("Nhập chuỗi ký tự: ")
words = []
word = " "
for c in Str:
    if c.isalnum():
        word += c
    else:
        if word:
            words.append(word)
            word = " "
if word:
    words.append(word)
for w in words:
    print(w)
    
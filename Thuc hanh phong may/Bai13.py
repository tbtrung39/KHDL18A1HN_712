W = input("Nhập chuỗi ký tự: ")
dictionary = {}
for char in W:

    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1
print("Từ điển đếm số lần xuất hiện của các ký tự:", dictionary)
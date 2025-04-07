W = input("Nhập vào chuỗi ký tự: ")

substrings_count = {}

for length in range(1, len(W) + 1):
    for i in range(len(W) - length + 1):
        substring = W[i:i + length]
        if substring in substrings_count:
            substrings_count[substring] += 1
        else:
            substrings_count[substring] = 1

print(substrings_count)
s = set()
print("Nhập từng ký tự, gõ 'ESC' để kết thúc:")

while True:
    ch = input("Ký tự: ")
    if ch == "ESC":
        break
    if len(ch) == 1:
        s.add(ch)

s = {c for c in s if not c.isdigit()}
print("Tập hợp sau khi xóa số:", s)

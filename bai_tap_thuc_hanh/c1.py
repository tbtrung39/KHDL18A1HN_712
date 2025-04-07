s = set()

while True:
    ch = input("Nhập 1 ký tự (gõ ESC để kết thúc): ")
    if ch == 'ESC':
        break
    s.add(ch)

for i in list(s):
    if '0' <= i <= '9':
        s.remove(i)

print("Tập hợp sau khi xóa ký tự số:", s)


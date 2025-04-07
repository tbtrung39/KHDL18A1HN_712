Numbers = []

while True:
    n = input("Nhập số tự nhiên (gõ 'x' để kết thúc): ")
    if n == 'x':
        break
    if n.isdigit():
        Numbers.append(int(n))

A = set(Numbers)

print("Danh sách Numbers:", Numbers)
print("Tập hợp A:", A)

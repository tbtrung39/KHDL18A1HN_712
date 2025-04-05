numbers = []
print("Nhập số tự nhiên (bấm 'q' để kết thúc):")
while True:
    num = input()
    if num == 'q':
        break
    if num.isdigit():
        numbers.append(int(num))
number_set = set(numbers)
print("Tập hợp A:", number_set)
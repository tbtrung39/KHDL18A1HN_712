lst3 = []
while True:
    num = int(input())
    if num == 0:
        break
    lst3.append(num)

lst3 = [1, 2, 3] + lst3
if len(lst3) >= 5:
    lst3 = lst3[:5] + [1, 2, 3] + lst3[5:]
lst3 += [1, 2, 3]
print("Danh sách sau khi chèn:", lst3)

k = int(input("Nhập k: "))
if 0 <= k < len(lst3):
    lst3.pop(k)
print("Danh sách sau khi xóa phần tử k:", lst3)

lst3.sort()
print("Danh sách tăng dần:", lst3)
lst3.sort(reverse=True)
print("Danh sách giảm dần:", lst3)
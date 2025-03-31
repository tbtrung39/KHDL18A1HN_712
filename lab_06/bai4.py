# bai4
lst = []
while True:
    num = int(input("Nhập số tự nhiên (nhập 0 để dừng): "))
    if num == 0:
        break
    lst.append(num)

print("Danh sách ban đầu:", lst)

insert_list = [1, 2, 3]

lst = insert_list + lst 
lst += insert_list  

if len(lst) >= 5:
    lst[5:5] = insert_list

print("Danh sách sau khi chèn:", lst)

k = int(input("Nhập vị trí phần tử cần xóa (bắt đầu từ 0): "))

if 0 <= k < len(lst):
    del lst[k]
    print("Danh sách sau khi xóa phần tử thứ", k, ":", lst)
else:
    print("Vị trí không hợp lệ!")

lst_tang_dan = sorted(lst)
print("Danh sách sắp xếp tăng dần:", lst_tang_dan)

lst_giam_dan = sorted(lst, reverse=True)
print("Danh sách sắp xếp giảm dần:", lst_giam_dan)

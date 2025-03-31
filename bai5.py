# bai 5
lst = list(map(int, input("Nhập danh sách số nguyên, cách nhau bởi dấu cách: ").split()))

if len(lst) > 1:
    lst.pop(0)  
    lst.pop(-1) 

if lst:
    min_val = min(lst)
    lst.remove(min_val)

print("Danh sách sau khi chỉnh sửa:", lst)

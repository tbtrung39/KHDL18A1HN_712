# Câu 4
lst = []
while True:
    num = int(input("Nhap so tu nhien (Nhap 0 de dung): "))
    if num == 0:
        break
    lst.append(num)
lst.insert(0, [1, 2, 3])
lst.append([1, 2, 3])
if len(lst) >= 5:
    lst.insert(5, [1, 2, 3])
k = int(input("Nhap vi tri phan tu can xoa: "))
if 0 <= k < len(lst):
    lst.pop(k)
else:
    print("Vi tri khong hop le")
lst_flat = []
for item in lst:
    if type(item) == list:
        for subitem in item:
            lst_flat.append(subitem)
    else:
        lst_flat.append(item)
lst_flat.sort()
print("Danh sach sau khi sap xep tang dan:", lst_flat)
lst_flat.sort(reverse=True)
print("Danh sach sau khi sap xep giam dan:", lst_flat)
# Cau 4.
def creatr_listA(n):
    listA = []
    for i in range(n):
        number = int(input("Nhap so nguyen: "))
        listA.append(number)
    return listA
def insert_recursive(listA, value, index):
    if index == 0:
        return [value] + listA
    else:
        return [listA[0]] +insert_recursive(listA[1:], value, index - 1)
n = int(input("Nhap so luong phan tu trong listA: "))
listA = creatr_listA(n)
print("ListA ba dau: ", listA)
x = int(input("Nhap so muon chen: "))
k = int(input("Nhap vi tri muon chen: "))
listA = insert_recursive(listA, x, k)
print("ListA sau khi chen: ", listA)
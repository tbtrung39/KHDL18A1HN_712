list1 = list(map(int, input("Nhập danh sách số: ").split()))
list2 = input("Nhập danh sách tên: ").split()

if len(list1) != len(list2):
    print("Hai danh sách không cùng độ dài!")
else:
    result_dict = {list1[i]: list2[i] for i in range(len(list1))}
    print(result_dict)
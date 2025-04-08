list1 = list(map(int, input("Nhập list1 (số, cách nhau bởi dấu cách): ").split()))
list2 = input("Nhập list2 (tên, cách nhau bởi dấu cách): ").split()

d = dict(zip(list1, list2))
print("Từ điển tạo được:", d)

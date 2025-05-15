n = int(input("Nhập số lượng phần tử n: "))
list1 = []
print("Nhập các số cho list1:")
for i in range(n):
    num = int(input(f"Nhập số thứ {i+1}: "))
    list1.append(num)
list2 = []
print("Nhập các tên cho list2:")
for i in range(n):
    name = input(f"Nhập tên thứ {i+1}: ")
    list2.append(name)
print("Nội dung từ điển:")
for i in range(n):
    print(f"<{list1[i]}> - <{list2[i]}>")
list1 = input("Nhập các phần tử list1 (cách nhau bởi dấu cách): ").split()
list2 = input("Nhập các phần tử list2 (cách nhau bởi dấu cách): ").split()
d = {f"<{a}>": f"<{b}>" for a, b in zip(list1, list2)}
print("Từ điển:")
for k, v in d.items():
    print(f"{k}: {v}")

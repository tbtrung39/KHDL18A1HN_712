lst1 = input("Nhập các phần tử list1 (cách nhau bởi dấu cách): ").split()
lst2 = input("Nhập các phần tử list2 (cách nhau bởi dấu cách): ").split()
m= {f"<{a}>": f"<{b}>" for a, b in zip(lst1, lst2)}
print("Từ điển:")
for k, v in m.items():
    print(f"{k}: {v}")
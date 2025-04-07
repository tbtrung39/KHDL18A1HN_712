list1 = input("Nhập danh sách 1 (Các phần tử cách nhảy bởi dấu cách):").split()
list2 = input("Nhập danh sách (các phần tử cách nhảy bởi dấu cách)").split()
tu_dien = {k: v for k, v in zip( list1, list2)}
print("tu_dien", tu_dien)

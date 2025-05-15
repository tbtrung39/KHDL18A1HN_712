List_ = [
    ["mon", 73],
    ["tue", 89],
    ["wed", 95],
    ["thu", 103],
    ["fri", 115],
    ["sat", 128],
    ["sun", 120]
]
print("Danh sach:", List_)
print("\nPhan tu thu hai cua sublist thu 3:", List_[2][1])
if len(List_) < 8:
    List_.append(["extra_day", 100])
print("\n Danh sach sau khi them (neu can):", List_)
print("\nTong sale value:", sum(x[1] for x in List_))
def tim_max_de_quy(lst, n):
    if n == 1:
        return lst[0]
    return max(lst[n - 1], tim_max_de_quy(lst, n - 1))
n = int(input("Nhập số lượng phần tử: "))
lst = []

for i in range(n):
    so = float(input(f"Nhập số thứ {i + 1}: "))
    lst.append(so)
ket_qua = tim_max_de_quy(lst, n)
print("Số lớn nhất là:", ket_qua)

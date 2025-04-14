def count_occurrences(n, values):
    return values.count(n)

n = int(input("Nhập số nguyên cần đếm: "))
values = list(map(int, input("Nhập danh sách số nguyên cách nhau bằng dấu cách: ").split()))
print("Số lần xuất hiện:", count_occurrences(n, values))
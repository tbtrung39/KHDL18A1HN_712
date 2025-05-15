def bai_6():
    n = int(input("Nhập số lượng phần tử n: "))
    lst = []
    print("Nhập", n, "số nguyên:")
    for i in range(n):
        x = int(input(f"Số thứ {i+1}: "))
        lst.append(x)
    A = set(lst)
    count_7_dau = 0
    for num in lst:
        if num == 7:
            count_7_dau += 1
        else:
            break
    print("Tập hợp A:", A)
    print("Số lượng số 7 xuất hiện liên tiếp đầu tiên:", count_7_dau)
bai_6()

A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")
digits_A = [c for c in A if c.isdigit()]
digits_B = [c for c in B if c.isdigit()]
if digits_A and digits_B:
    expression = "+".join(digits_A) + "=" + "+".join(digits_B)
    sum_A = sum(int(c) for c in digits_A)
    sum_B = sum(int(c) for c in digits_B)
    if sum_A == sum_B:
        print("Đẳng thức đúng:", expression)
    else:
        print("Không tồn tại cách đặt!")
else:
    print("Không thể tạo biểu thức!")

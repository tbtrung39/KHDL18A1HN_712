X, Y = map(int, input("Nhập X và Y (cách nhau bằng dấu phẩy): ").split(","))
mang_2_chieu = [[i * j for j in range(Y)] for i in range(X)]
print("Mảng 2 chiều:")
for hang in mang_2_chieu:
    print(hang)
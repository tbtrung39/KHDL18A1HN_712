# Câu 6. Vòng lặp while
# a) Viết chương trình in ra các số từ 1 đến 10 bằng while.
# b) Tính tổng các số chia hết cho 3 từ 1 đến 50.

# a) 
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

# b) 
i = 1
tong_3 = 0
while i <= 50:
    if i % 3 == 0:
        tong_3 += i
    i += 1
print("Tổng các số chia hết cho 3 từ 1 đến 50 là:", tong_3)

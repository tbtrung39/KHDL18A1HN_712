# Câu 8. Vòng lặp for
# a) Viết chương trình in ra các số từ 1 đến 20.
# b) Tính tổng các số lẻ từ 1 đến 100.

# a) 
for i in range(1, 21):
    print(i)
print()

# b) 
tong = sum(i for i in range(1, 101) if i % 2 != 0)
print(tong)

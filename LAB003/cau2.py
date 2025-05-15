n = int(input("Nhập n: "))
for số in range(1, n):  
    if sum(ước for ước in range(1, số) if số % ước == 0) == số:
        print(số, end=" ")
else:
    print("\nHoàn thành tìm số hoàn hảo!")

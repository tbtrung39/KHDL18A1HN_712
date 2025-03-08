#Câu 4:
n = int(input("Nhập số nguyên dương n: "))
if n < 2:
    print(n, "không phải số nguyên tố")
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            print(n, "không phải số nguyên tố")
            break
        i += 1
    else:
        print(n, "là số nguyên tố")

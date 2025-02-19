def chu_so_hang_tram(n):
    if n < 100:
        return 0
    else:
        return (n // 100) % 10

n = int(input("Nhập vào một số nguyên: "))
print(chu_so_hang_tram(n))
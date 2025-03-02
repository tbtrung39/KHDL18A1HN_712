def phan_tich_thua_so_nguyen_to(n):

    if n <= 1:
        print("Không thể phân tích thừa số nguyên tố cho số này.")
        return
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:  
            print(i, end=" * ")
            n //= i  
    if n > 1:
        print(n, end="")

n = int(input("Nhập vào số nguyên dương n: "))
phan_tich_thua_so_nguyen_to(n)

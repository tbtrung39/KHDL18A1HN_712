import random

def tao_hoan_vi_ngau_nhien(n):
    A = list(range(1, n + 1))
    random.shuffle(A)
    return A

def main():
    n = int(input("Nhập số tự nhiên n: "))
    if n <= 0:
        print("Vui lòng nhập số nguyên dương.")
        return
    
    result = tao_hoan_vi_ngau_nhien(n)
    print(f"Hoán vị ngẫu nhiên của dãy từ 1 đến {n} là:")
    print(result)

main()

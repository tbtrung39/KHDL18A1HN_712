def la_so_nguyen_to(num):
    """Kiểm tra xem một số có phải là số nguyên tố hay không."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def in_n_so_nguyen_to(n):
    """In ra n số nguyên tố đầu tiên."""
    count = 0
    num = 2
    while count < n:
        if la_so_nguyen_to(num):
            print(num, end=" ")
            count += 1
        num += 1
    print()

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Nhập số tự nhiên n: "))
            if n > 0:
                break
            else:
                print("Vui lòng nhập một số nguyên dương.")
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")

    print(f"\nDãy {n} số nguyên tố đầu tiên là:")
    in_n_so_nguyen_to(n)
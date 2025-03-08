def tong_chu_so(n):
    """Hàm tính tổng các chữ số của một số"""
    return sum(int(digit) for digit in str(abs(n)))

num = int(input("Nhập một số nguyên: "))

print(f"Tổng các chữ số của {num} là: {tong_chu_so(num)}")

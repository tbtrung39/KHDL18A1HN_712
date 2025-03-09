def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def main():
    while True:
        try:
            a = int(input("Nhập số nguyên thứ nhất: "))
            b = int(input("Nhập số nguyên thứ hai: "))
            if a == 0 or b == 0:
                print("Bội chung nhỏ nhất của số 0 với bất kỳ số nào không xác định. Vui lòng nhập lại.")
                continue
            result = lcm(a, b)
            print(f"Bội chung nhỏ nhất của {a} và {b} là: {result}")
            break
        except ValueError:
            print("Vui lòng nhập các số nguyên hợp lệ!")
main()

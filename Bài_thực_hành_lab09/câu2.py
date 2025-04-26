def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcd_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return gcd(numbers[0], gcd_list(numbers[1:]))

n = int(input("Nhập số lượng số nguyên n: "))
numbers = []

for i in range(n):
    num = int(input(f"Nhập số thứ {i+1}: "))
    numbers.append(num)

print("Ước chung lớn nhất của các số là:", gcd_list(numbers))

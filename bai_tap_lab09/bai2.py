import math

def gcd_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = math.gcd(result, num)
    return result

n = int(input("Nhập số lượng phần tử: "))
numbers = [int(input(f"Nhập số thứ {i+1}: ")) for i in range(n)]

print("Ước chung lớn nhất là:", gcd_list(numbers))

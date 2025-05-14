def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input("Nhập số lượng số cần tính UCLN: "))
nums = [int(input(f"Nhập số thứ {i+1}: ")) for i in range(n)]

result = nums[0]
for num in nums[1:]:
    result = ucln(result, num)

print("UCLN của các số là:", result)

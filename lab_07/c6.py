def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

numbers = []
print("Nhập 50 số tự nhiên:")
while len(numbers) < 50:
    try:
        n = int(input(f"Nhập số thứ {len(numbers)+1}: "))
        numbers.append(n)
    except:
        print("Nhập sai, nhập lại.")

# Tìm số nguyên tố đầu tiên
first_prime = None
for num in numbers:
    if is_prime(num):
        first_prime = num
        break

if first_prime:
    print("Số nguyên tố đầu tiên là:", first_prime)
else:
    print("Không có số nguyên tố trong danh sách.")

# Câu 5.
Str = input("Nhap chuỗi số: ")
is_perfect = False
if Str.isdigit():
    num = int(Str)
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    if sum_divisors == num:
        is_perfect = True
print("Số này là số hoàn hảo." if is_perfect else "Số này không phải số hoàn hảo.")

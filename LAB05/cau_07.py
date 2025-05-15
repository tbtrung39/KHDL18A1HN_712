Str = input("Nhập chuỗi ký tự: ")
filtered = ""
for c in Str:
    if '0' <= c <= '9':
        filtered += c
if filtered:
    num = int(filtered)
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    print("Số này là số hoàn hảo." if sum_divisors == num else "Số này không phải số hoàn hảo.")
else:
    print("Không có số hợp lệ trong chuỗi.")
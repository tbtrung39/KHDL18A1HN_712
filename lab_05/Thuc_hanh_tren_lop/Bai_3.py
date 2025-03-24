n = int(input("Nhập một số nguyên: "))
nhiphan = ""
if n == 0:
    nhiphan = "0"
while n > 0:
    nhiphan = str(n % 2) + nhiphan
    n //= 2
print("Số nhị phân tương ứng:", nhiphan)
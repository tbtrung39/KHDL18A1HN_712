while True:
    n = int(input("Nhập n (số nguyên dương): "))
    if n > 0:
        break
    print("Vui lòng nhập lại!")

s4 = sum(i for i in range(1, n + 1))  # S4 = 1 + 2 + 3 + ... + n
s5 = sum(2 * i + 1 for i in range(n))  # S5 = 1 + 3 + 5 + ...
s6 = sum(2 * i for i in range(1, n + 1))  # S6 = 2 + 4 + 6 + ...

print(f"S4 = {s4}")
print(f"S5 = {s5}")
print(f"S6 = {s6}")
def calculate_X(n, X_values):
    if n == 0:
        return 1 
    else:
        total = 0
        for i in range(n):
            total += (n - i) ** 2 * X_values[i]  
        return total
    
n = int(input("Nhập số n: "))

X_values = [1]  # X0 = 1
for i in range(1, n + 1):
    X_values.append(calculate_X(i, X_values))

print(f"X_{n} = {X_values[n]}")

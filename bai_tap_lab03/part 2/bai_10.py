
n = int(input("Nhap vao n= "))
i = 2
while n > 1:
    while n % i == 0:
        print(i, "", end="") 
        n //= i
    i += 1
print()
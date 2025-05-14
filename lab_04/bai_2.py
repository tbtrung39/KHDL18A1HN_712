n = int(input("Nhập n: "))
# Câu a
s1 = 0
for i in range(1, n+1):
    s1 += (-1)**(i+1) / i
print("s1=", s1)

# Câu b
s2 = 0
for i in range(1, n+1):
    s2 += 1 / (i * (i+1))
print("s2=", s2)

# Câu c
s3 = 0
for i in range(2, n+2):
    s3 += 1 / (i**0.5)
print("s3=", s3)
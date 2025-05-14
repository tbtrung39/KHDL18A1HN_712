# a
n = int(input('Nhập số nguyên dương n: '))
if n <= 0:
    print('Vui lòng nhập một số nguyên dương lớn hơn 0.')
    n = int(input('Nhập số nguyên dương n: '))
S1 = n * (n + 1) // 2  
print('S1 =', S1)

# b
n = int(input('Nhập số nguyên dương n: '))
if n <= 0:
    print('Vui lòng nhập một số nguyên dương > 0')
    n = int(input('Nhập số nguyên dương n: '))
S2 = (n + 1) ** 2
print('S2 =', S2)


# c
n = int(input('Nhập số nguyên dương n: '))
if n <= 0:
    print('Vui lòng nhập một số nguyên dương lớn hơn 0.')
    n = int(input('Nhập số nguyên dương n: '))
S3 = n * (n + 1)
print('S3 =', S3)



# Cau 2.

lst = [1, 2, 3, 4, 5]
i = 0
sum = 0
try:
    while True:
        sum = sum + lst[i]
        i = i + 1
except IndexError:
    pass
print("Tong day so da cho la: ",sum )
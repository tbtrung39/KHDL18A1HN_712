num = int(input("Nhập một số nguyên dương: "))
while num < 0:
    num = int(input("Vui lòng nhập số nguyên dương: "))
so_chu = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
num_str = str(num)
for digit in num_str:
    print(so_chu[int(digit)], end=" ")

print() 
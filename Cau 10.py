# Câu 10. Biến và kiểu dữ liệu
# a) Khai báo ba biến số nguyên và thực hiện phép toán cộng, trừ, nhân, chia trên chúng.
# b) Kiểm tra xem một số nhập vào có phải là số nguyên tố hay không.

# a.
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
tong = a + b + c
hieu = a - b - c
tich = a * b * c
if c != 0:  
    thuong = a / b / c
else:
    thuong = "Không thể chia cho 0"
print("Tổng của ba số là:", tong)
print("Hiệu của ba số là:", hieu)
print("Tích của ba số là:", tich)
print("Thương của ba số là:", thuong)

# b.
def kiem_tra_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập một số: "))
if kiem_tra_nguyen_to(n):
    print(n, "là số nguyên tố.")
else:
    print(n, "không phải là số nguyên tố.")

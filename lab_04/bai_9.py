x=int(input("Nhập số nguyên dương: "))
while x<0:
    x=int(input("Không hợp lệ.Vui lòng nhập sô nguyên dương"))
tong=0
while x>0:
    tong+=x%10
    x//=10
print("Tổng các chữ số là: ",tong)
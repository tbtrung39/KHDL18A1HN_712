# Cau 1.

while True:
    try:
        num = int(input("Nhap mot so nguyen: "))
        break
    except ValueError:
        print("Ban da nhap sai!. Ban can nhap vao mot so nguyen!")
print("Ban nhap dung roi!")
print("So da nhap la", num)
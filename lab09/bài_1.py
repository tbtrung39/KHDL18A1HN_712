def max(a,b):
    if a > b:
        return a
    else:
        return b

def tim_max(x,y,z):
    return max(max(x,y),z)

a = int(input("Nhập số thứ nhất : "))
b = int(input("Nhập số thứ hai : "))
c = int(input("Nhập số thứ ba : "))

max_value = tim_max(a,b,c)
print("Số lớn nhất là : ",max_value)
a = []
while True:
    num = int(input("Nhập một số tự nhiên (nhập 0 để dừng): "))
    if num == 0:
        break
    a.append(num)

so_duong = [num for num in a if num > 0]  
sokhongduong = [num for num in a if num <= 0] 
a = so_duong + sokhongduong  

print("Danh sách sau khi chuyển các phần tử dương lên đầu:",a)

m = int(input("Nhập số m để chèn vào danh sách: "))
a.insert(0, m)
a.append(m)
if len(a) >= 5:
    a.insert(5, m)
print("Danh sách sau khi chèn số m vào đầu, cuối và vị trí thứ 5:", a)


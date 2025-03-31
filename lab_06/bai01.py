a=[2,-4,1,9,-3,6,3,-2,6,8]
s1=0
for i in a:
    s1 += i
print("Tổng các phần tử trong danh sách a=  ",s1)

dem= 0
s2 = 0
for n in a:
    if n > 0:
        dem += 1
        s2 += n
print("Số lượng các số hạng dương:", dem)
print("Tổng các số hạng dương:", s2)

for i in range(len(a)):
    if a[i] < 0:
        print("Vị trí âm đầu tiên trong danh sách", i)
        break

for i in range(len(a)-1,0,-1):
    if a[i] > 0:
        print("Vị trí dương cuối cùng trong danh sách:", i)
        break
b = a.copy()
b.sort()
u = b.pop()
print("Phần tử lớn nhất:",u , "vị trí", a.index(u))

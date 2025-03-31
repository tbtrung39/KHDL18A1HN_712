List=[["mon",73],["tue",89],["wed",95],['thu',103],['fri',115],['sat',128],['sun',120]]
print("danh sach list: ")
for i in List:
    print(i)
svalue=[]
for i in List:
    svalue.append(i[1])
print("Danh sach cac gia tri sale: ",svalue)

import random
test=[]
if len(test)<3:
    while len(test)<3:
        snn=random.choice(List)
        if snn not in test:
            test.append(snn)
print("Danh sach test: ",test)
tongsale=0
for i in List:
    if i[0] in ["tue",'sat','sun']:
        tongsale+=i[1]
print('tong gia tri sale cua thu 3, thu 5 va thu 7 la:' ,tongsale)
#Câu 15:
list1=list(map(int,input("Nhập số khác nhau:").split()))
list2=input("Nhập tên tương ứng:")
tu_dien={}
for i in range(len(list1)):
    tu_dien[list1[i]]=list2[i]
print(tu_dien)
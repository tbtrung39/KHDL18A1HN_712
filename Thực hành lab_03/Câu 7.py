#Câu 7:
n=int(input("Nhập số nguyên n: "))
s=0
for i in range(1,n+1):
    s+=1/i 
    i+=1
print("Tổng nghịch đảo của",n,"số nguyên đầu tiên là: ",s)


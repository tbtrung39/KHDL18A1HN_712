#Câu 8:
A={10,3.14,"Hello",-5,2.17,"Python",42,0.99,"AI"}
int_count=sum(isinstance(x,int)for x in A)
float_count=sum(isinstance(x,float)for x in A)
str_count=sum(isinstance(x,str)for x in A)
print("tập hợp A:",A)
print("số phần tử là số nguyên:", int_count)
print("số phần tử là số thực:", float_count)
print("số phần tử là chuỗi ký tự:", str_count)
